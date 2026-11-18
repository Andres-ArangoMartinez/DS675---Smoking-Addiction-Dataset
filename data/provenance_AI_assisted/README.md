# Dataset provenance verification - AI-assisted

This folder reproduces the provenance and file checks summarized in
[data/README.md](../README.md). The verifier uses Python's standard library;
no packages, credentials, or notebook execution are needed. It reads the common
raw CSV and leaves datasets and earlier audit results unchanged.

## Evidence and calculations

[sources.json](sources.json) records the selected Kaggle version, public URLs,
pinned GitHub commit, and expected values already documented by this project.
It also identifies the unchanged saved
[Kaggle metadata response](evidence/kaggle_metadata_20261116.json) and its SHA-256.
That response was saved during the provenance work recorded on November 16, 2026;
it is historical evidence, rather than a new retrieval. The snapshot hash detects
changes relative to the source record; it is not a publisher signature.

[verify.py](verify.py) performs these checks:

1. **File identity:** calculate byte size, SHA-256, and the Git blob identifier
   (`SHA1(b"blob " + byte_count + b"\0" + file_bytes)`). Compare with the recorded
   reference values; a matching hash identifies content, not download origin.
2. **README measurements:** parse logical CSV records; count rows, columns,
   participants, duplicate participant-day keys, and blank target cells. Confirm
   that every participant has exactly days 1 through 30. Zero is an observed
   score; blank targets remain missing. This small summary does not replace the
   [full statistical audit](../../work/andres/02_dataset_description/dataset_audit_AI_assisted/README.md).
3. **Publisher metadata:** check the saved response's hash, dataset ID, owner/slug,
   version, and reported license. CC0 is attributed to the publisher's metadata;
   the CSV cannot establish a reuse license.
4. **Git storage:** inspect the actual Git index with `git ls-files` and the
   effective ignore rules with `git check-ignore --no-index`. Confirm that the
   raw CSV is tracked, while new raw/processed files match ignore rules and the
   named local processed CSV is not tracked. GitHub Desktop's bundled Git is
   discovered on Windows when Git is absent from PATH; `--git` can specify it.
5. **Optional external comparison:** compare the local CSV byte for byte with
   the version-specific Kaggle archive and the CSV at the pinned GitHub commit.
   Online mode also checks current Kaggle metadata against the selected values.

## Reproduce from the repository root

Run the local checks, using the bundled metadata snapshot:

```powershell
python data/provenance_AI_assisted/verify.py
```

Retrieve the public sources again and compare them in memory:

```powershell
python data/provenance_AI_assisted/verify.py --online --output tmp/provenance_online.json
```

The online run downloads the version-1 ZIP, the pinned GitHub CSV, and current
metadata. It never extracts or replaces the raw CSV. Public endpoints can fail,
and current metadata can change; either condition is reported explicitly.
Choose a new `--output` filename for each saved run: existing reports are never
overwritten. Without `--output`, JSON is printed without creating a report.

For an offline comparison with existing downloaded files, supply their paths:

```powershell
python data/provenance_AI_assisted/verify.py --kaggle-archive 'path/to/kaggle_v1.zip' --github-csv 'path/to/github_copy.csv'
```

These are user-supplied comparison files; their byte equality alone does not
authenticate their origin. The program has no dependency on the old `tmp/`
folder. New downloads and optional report files are the only additional inputs
or outputs; no model fitting or temporal-protocol validation occurs.

Exit codes: `0` means all performed checks passed, `1` means a comparison failed,
and `2` means an input, network, Git, or output error prevented a check. Inspect
the JSON `summary`: offline mode marks external checks `not_checked` and reports
`local_checks_passed`, never `all_checks_passed` when evidence was not inspected.

Run the synthetic regression checks:

```powershell
python -m unittest discover -s data/provenance_AI_assisted -p test_verify.py -v
```

The tests cover duplicate keys, blank versus zero targets, malformed/empty CSVs,
ambiguous ZIP members, absent licensing metadata, and report preservation.

## Recorded verification

The [November 18, 2026 online run](results/verification_20261118.json) passed all
27 checks, including direct byte comparisons with both public CSV sources and
current Kaggle metadata. The offline run passed 19 checks and marked three
external checks as not performed; the saved-file comparison passed 23 checks
and left current metadata unqueried. All six regression tests passed.
These counts describe assertions in this verifier, not statistical techniques.
The recorded JSON is evidence of that execution; rerun the commands to inspect
the current sources and Git state. Raw data, notebooks, and previous statistical
audit outputs were not modified.
