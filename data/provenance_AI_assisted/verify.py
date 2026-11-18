"""Reproduce data/README.md checks without changing data or earlier audit outputs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.request import Request, urlopen
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MAX_DOWNLOAD = 20_000_000


def check(name, actual, expected):
    return {"name": name, "status": "passed" if actual == expected else "failed",
            "actual": actual, "expected": expected}


def csv_checks(raw, expected):
    """Count logical records and participant-day keys using only observed cells."""
    reader = csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline=""), strict=True)
    header = next(reader, None)
    if not header:
        raise ValueError("CSV has no header.")
    if len(header) != len(set(header)):
        raise ValueError("Duplicate column names prevent unambiguous checks.")
    indices = [header.index(c) for c in
               ("Participant_ID", "Day_Number", "Overall_Craving_Score")]
    panels, keys, rows, duplicates, missing = {}, set(), 0, 0, 0
    for row in reader:
        if len(row) != len(header):
            raise ValueError(f"Logical record {rows + 2} has the wrong field count.")
        participant, day_text, target = (row[i] for i in indices)
        if not participant or not day_text:
            raise ValueError("Missing participant-day key.")
        day = int(day_text)
        key = (participant, day)
        duplicates += key in keys
        keys.add(key)
        panels.setdefault(participant, []).append(day)
        rows += 1
        missing += target.strip() == ""
    digest = hashlib.sha256(raw).hexdigest()
    blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
    results = [check("csv_bytes", len(raw), expected["bytes"]),
               check("csv_sha256", digest, expected["sha256"]),
               check("csv_git_blob_sha1", blob, expected["git_blob_sha1"]),
               check("rows", rows, expected["rows"]),
               check("columns", len(header), expected["columns"]),
               check("participants", len(panels), expected["participants"]),
               check("duplicate_participant_day_keys", duplicates,
                     expected["duplicate_participant_day_keys"]),
               check("missing_Overall_Craving_Score", missing,
                     expected["missing_Overall_Craving_Score"])]
    complete = bool(panels) and all(sorted(days) == expected["days_per_participant"]
                                    for days in panels.values())
    results.append(check("every_participant_has_exact_day_coverage", complete, True))
    return results


def metadata_checks(metadata, expected, prefix):
    if not isinstance(metadata, dict):
        raise ValueError("Metadata response must be a JSON object.")
    fields = {"id": expected["id"], "ref": expected["ref"],
              "currentVersionNumber": expected["version"],
              "licenseName": expected["reported_license"]}
    return [check(f"{prefix}/{key}", metadata.get(key), value)
            for key, value in fields.items()]


def archive_csv(raw_zip, filename):
    """Read one unambiguous member in memory; never extract into data/raw/."""
    with zipfile.ZipFile(io.BytesIO(raw_zip)) as archive:
        matches = [i for i in archive.infolist()
                   if not i.is_dir() and Path(i.filename).name == filename]
        if len(matches) != 1:
            raise ValueError("Archive must contain exactly one matching CSV.")
        if matches[0].file_size > MAX_DOWNLOAD:
            raise ValueError("CSV archive member exceeds the download limit.")
        return archive.read(matches[0])


def download(url):
    request = Request(url, headers={"User-Agent": "DS675-Provenance-Verification/1.0"})
    with urlopen(request, timeout=25) as response:
        raw = response.read(MAX_DOWNLOAD + 1)
    if len(raw) > MAX_DOWNLOAD:
        raise ValueError("Response exceeds the download limit.")
    return raw


def find_git(explicit=None):
    if explicit:
        return explicit
    found = shutil.which("git")
    if found:
        return found
    # GitHub Desktop bundles Git even when git.exe is absent from PATH.
    local = os.environ.get("LOCALAPPDATA")
    if local:
        candidates = list((Path(local) / "GitHubDesktop").glob(
            "app-*/resources/app/git/cmd/git.exe"))
        if candidates:
            return str(max(candidates, key=lambda p: p.stat().st_mtime))
    raise OSError("Git not found. Put Git on PATH or supply --git path/to/git.exe.")


def git_checks(executable, csv_path):
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")

    def git(*args, allowed=(0,)):
        result = subprocess.run([executable, "-C", str(ROOT), *args],
                                capture_output=True, text=True, env=env,
                                timeout=15)
        if result.returncode not in allowed:
            raise RuntimeError(result.stderr.strip() or "Git inspection failed.")
        return result

    actual_root = Path(git("rev-parse", "--show-toplevel").stdout.strip()).resolve()
    tracked = git("ls-files", "--", csv_path).stdout.splitlines()
    ignored = git("check-ignore", "--no-index", "--", csv_path, allowed=(0, 1))
    processed = "data/processed/next_day_protocol_v1.csv"
    return [check("git/repository_root", str(actual_root), str(ROOT)),
            check("git/raw_csv_tracked", csv_path in tracked, True),
            check("git/raw_rule_ignores_new_files", ignored.returncode == 0, True),
            check("git/processed_csv_tracked",
                  bool(git("ls-files", "--", processed).stdout.strip()), False),
            check("git/processed_rule_ignores_new_files",
                  git("check-ignore", "--no-index", "--", processed,
                      allowed=(0, 1)).returncode == 0, True)]


def run(args):
    record = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
    expected = record["csv"]
    raw = (ROOT / expected["path"]).read_bytes()
    results = []

    def attempt(name, operation):
        try:
            results.extend(operation())
        except (OSError, ValueError, KeyError, csv.Error, zipfile.BadZipFile,
                RuntimeError, subprocess.TimeoutExpired) as error:
            results.append({"name": name, "status": "error", "message": str(error)})

    attempt("local_csv", lambda: csv_checks(raw, expected))
    snapshot = record["metadata_snapshot"]

    def saved_metadata():
        content = (HERE / snapshot["path"]).read_bytes()
        return [check("saved_metadata/sha256", hashlib.sha256(content).hexdigest(),
                      snapshot["sha256"]),
                *metadata_checks(json.loads(content), record["dataset"], "saved_metadata")]

    attempt("saved_metadata", saved_metadata)
    attempt("git", lambda: git_checks(find_git(args.git), expected["path"]))
    filename = Path(expected["path"]).name
    sources = record["sources"]
    for name, path, url, is_archive in (
        ("kaggle_csv", args.kaggle_archive, sources["archive_url"], True),
        ("github_csv", args.github_csv, sources["github_csv_url"], False),
    ):
        if not path and not args.online:
            results.append({"name": name, "status": "not_checked",
                            "message": "Use --online or supply the saved comparison file."})
            continue

        def compare(path=path, url=url, is_archive=is_archive, name=name):
            content = Path(path).read_bytes() if path else download(url)
            content = archive_csv(content, filename) if is_archive else content
            prefix = name + ("/saved_file" if path else "/download")
            return [check(prefix + "/byte_identical", content == raw, True),
                    check(prefix + "/sha256", hashlib.sha256(content).hexdigest(),
                          expected["sha256"])]

        attempt(name, compare)
    if args.online:
        attempt("live_metadata", lambda: metadata_checks(
            json.loads(download(sources["metadata_url"])), record["dataset"], "live_metadata"))
    else:
        results.append({"name": "live_metadata", "status": "not_checked",
                        "message": "The bundled historical metadata was checked instead."})
    counts = {status: sum(c["status"] == status for c in results)
              for status in ("passed", "failed", "error", "not_checked")}
    status = ("error" if counts["error"] else "failed" if counts["failed"] else
              "local_checks_passed" if counts["not_checked"] else "all_checks_passed")
    return {"status": status, "mode": "online" if args.online else "offline",
            "summary": counts, "sources": sources, "checks": results,
            "limits": record["evidence_limits"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", action="store_true", help="Fetch the three public source URLs.")
    parser.add_argument("--kaggle-archive", type=Path, help="Compare an existing ZIP without extracting it.")
    parser.add_argument("--github-csv", type=Path, help="Compare an existing mirror CSV without changing it.")
    parser.add_argument("--git", help="Path to Git if automatic discovery is unavailable.")
    parser.add_argument("--output", type=Path, help="Create a new JSON report; never overwrite an existing file.")
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error("Output already exists; choose a new report path.")
    try:
        report = run(args)
        content = json.dumps(report, indent=2, ensure_ascii=True) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open("x", encoding="utf-8") as stream:
                stream.write(content)
        print(content, end="")
    except (OSError, ValueError, KeyError) as error:
        print(f"Verification stopped: {error}", file=sys.stderr)
        return 2
    return 2 if report["summary"]["error"] else 1 if report["summary"]["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
