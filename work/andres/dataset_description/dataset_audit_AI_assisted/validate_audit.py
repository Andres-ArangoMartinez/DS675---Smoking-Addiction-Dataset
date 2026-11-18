"""Independently verify exported results and test temporal/ingestion edge cases.

The full-file numerical checks use csv, statistics, dictionaries, and arithmetic
from Python's standard library rather than the pandas/numpy audit calculations.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import statistics
import tempfile
import unittest
from collections import Counter, defaultdict
from pathlib import Path

import audit
import pandas as pd


def independent_checks(csv_path: Path, results_path: Path) -> dict:
    """Recalculate measurements from raw CSV strings through a second route."""
    raw = csv_path.read_bytes()
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    result = json.loads(results_path.read_text(encoding="utf-8"))
    checks = []

    def check(name, actual, expected, tolerance=0):
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            passed = math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance)
        else:
            passed = actual == expected
        checks.append({"metric": name, "passed": passed, "independent": actual, "audit": expected})

    check("raw_sha256", hashlib.sha256(raw).hexdigest(), result["provenance"]["sha256"])
    check("original_description_sha256", hashlib.sha256(audit.ORIGINAL.read_bytes()).hexdigest(), result["provenance"]["reference_document_sha256"])
    check("audit_code_sha256", hashlib.sha256(Path(audit.__file__).read_bytes()).hexdigest(), result["provenance"]["audit_code_sha256"])
    check("reference_values_sha256", hashlib.sha256(audit.REFERENCE.read_bytes()).hexdigest(), result["provenance"]["reference_values_sha256"])
    check("rows", len(rows), result["structure"]["rows"])
    check("columns", len(rows[0]), result["structure"]["columns"])
    participants = {r["Participant_ID"] for r in rows}
    check("participants", len(participants), result["structure"]["participants"])
    check("duplicate_keys_excess", len(rows) - len({(r["Participant_ID"], r["Day_Number"]) for r in rows}), result["structure"]["duplicate_keys_excess"])
    check("duplicate_rows_excess", len(rows) - len({tuple(r.values()) for r in rows}), result["structure"]["duplicate_rows_excess"])
    check("incomplete_rows", sum(any(v == "" for v in row.values()) for row in rows), result["missingness"]["rows_with_missing"])
    missing_total = 0
    for column in rows[0]:
        missing = sum(row[column] == "" for row in rows)
        missing_total += missing
        check("missing/" + column, missing, result["missingness"]["by_column"][column]["missing"])
    check("missing_cells", missing_total, result["missingness"]["missing_cells"])

    def quantile(values, probability):
        ordered = sorted(values)
        h = (len(ordered) - 1) * probability
        lo, hi = math.floor(h), math.ceil(h)
        return ordered[lo] + (h - lo) * (ordered[hi] - ordered[lo])

    for column, expected in result["numeric"].items():
        values = [float(row[column]) for row in rows if row[column] != ""]
        q1, q3 = quantile(values, 0.25), quantile(values, 0.75)
        actual = {
            "observed": len(values), "min": min(values), "max": max(values),
            "mean": statistics.mean(values), "median": statistics.median(values),
            "sample_variance": statistics.variance(values), "sample_std": statistics.stdev(values),
            "q1": q1, "q3": q3, "iqr": q3 - q1,
        }
        for metric, value in actual.items():
            check(f"numeric/{column}/{metric}", value, expected[metric], 1e-9)
    profiles = {}
    for row in rows:
        profile = tuple(row[c] for c in audit.PROFILE)
        if row["Participant_ID"] in profiles:
            if profile != profiles[row["Participant_ID"]]:
                raise AssertionError("Independent profile invariance check failed.")
        else:
            profiles[row["Participant_ID"]] = profile
    for column, expected in result["categorical_counts"].items():
        if column in audit.DEMOGRAPHICS:
            index = audit.PROFILE.index(column)
            counts = Counter(profile[index] for profile in profiles.values() if profile[index] != "")
        else:
            counts = Counter(row[column] for row in rows if row[column] != "")
        check("categories/" + column, dict(counts), expected)
    observed = [float(row[audit.TARGET]) for row in rows if row[audit.TARGET] != ""]
    bins = [0] * 10
    for value in observed:
        if 0 <= value <= 10:
            bins[min(int(value), 9)] += 1
    check("target_histogram_counts", bins, result["target"]["histogram_counts"])

    values_by_key = {(r["Participant_ID"], int(r["Day_Number"])): float(r[audit.TARGET]) for r in rows if r[audit.TARGET] != ""}
    person_values = defaultdict(list)
    for (person, day), value in values_by_key.items():
        person_values[person].append(value)
    means = {person: statistics.mean(values) for person, values in person_values.items()}
    # Dictionary lookup of day+1 is independent of the audit's groupby/shift route.
    a, b, centered_a, centered_b = [], [], [], []
    for (person, day), value in values_by_key.items():
        if (person, day + 1) in values_by_key:
            following = values_by_key[(person, day + 1)]
            a.append(value)
            b.append(following)
            centered_a.append(value - means[person])
            centered_b.append(following - means[person])
    temporal = result["longitudinal"]
    check("valid_adjacent_pairs", len(a), temporal["valid_adjacent_pairs"])
    check("pooled_pearson", statistics.correlation(a, b), temporal["pooled_lag1_pearson"], 1e-12)
    check("person_centered_pearson", statistics.correlation(centered_a, centered_b), temporal["person_centered_lag1_pearson"], 1e-12)
    check("person_mean_min", min(means.values()), temporal["person_mean_min"], 1e-12)
    check("person_mean_max", max(means.values()), temporal["person_mean_max"], 1e-12)
    grand_mean = statistics.mean(observed)
    ss_total = math.fsum((v - grand_mean) ** 2 for v in observed)
    ss_within = math.fsum((v - means[person]) ** 2 for person, values in person_values.items() for v in values)
    ss_between = math.fsum(len(values) * (means[person] - grand_mean) ** 2 for person, values in person_values.items())
    for metric, value in {"total": ss_total, "within": ss_within, "between": ss_between}.items():
        check("sum_of_squares/" + metric, value, temporal["sum_of_squares"][metric], 1e-8)
    return {"method": "Independent standard-library parsing, statistics, and keyed day+1 lookups", "checks": len(checks), "passed": sum(c["passed"] for c in checks), "failed": [c for c in checks if not c["passed"]]}


class AuditEdgeCases(unittest.TestCase):
    """Protect against plausible temporal and input-handling mistakes."""

    def test_gaps_missing_values_and_shuffled_rows_do_not_create_pairs(self):
        frame = pd.DataFrame({
            "Participant_ID": ["B", "A", "B", "A", "B", "A", "B"],
            "Day_Number": [4, 4, 2, 1, 3, 2, 1],
            audit.TARGET: [13.0, 4.0, float("nan"), 1.0, 12.0, 2.0, 10.0],
        })
        result, tables = audit.longitudinal_summary(frame)
        pairs = tables["adjacent_pairs"]
        actual = set(zip(pairs["Participant_ID"], pairs["Day_Number"], pairs["next_day"]))
        self.assertEqual(actual, {("A", 1, 2), ("B", 3, 4)})
        self.assertEqual(result["potential_adjacent_pairs"], 4)
        self.assertEqual(result["pairs_excluded_for_missing_values"], 2)
        a_pair = pairs.loc[pairs["Participant_ID"].eq("A")].iloc[0]
        self.assertAlmostEqual(a_pair["deviation"], 1 - 7 / 3)

    def test_duplicate_keys_are_not_silently_resolved(self):
        frame = pd.DataFrame({"Participant_ID": ["A", "A"], "Day_Number": [1, 1], audit.TARGET: [1.0, 2.0]})
        result, tables = audit.longitudinal_summary(frame)
        self.assertTrue(result["status"].startswith("not_computed"))
        self.assertEqual(tables, {})

    def test_missing_keys_prevent_ambiguous_temporal_pairs(self):
        frame = pd.DataFrame({"Participant_ID": ["A", None], "Day_Number": [1, 2], audit.TARGET: [1.0, 2.0]})
        result, _ = audit.longitudinal_summary(frame)
        self.assertTrue(result["status"].startswith("not_computed"))

    def test_different_hash_requires_explicit_opt_in(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "different.csv"
            path.write_text("x\n1\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "hash differs"):
                audit.load_data(path)

    def test_malformed_width_is_rejected_before_dataframe_loading(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "malformed.csv"
            path.write_text("x,y\n1,2,3\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "structure is ambiguous"):
                audit.load_data(path, allow_different_input=True)


def main() -> int:
    output = audit.HERE / "results"
    independent = independent_checks(audit.DEFAULT_CSV, output / "audit_results.json")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AuditEdgeCases)
    tests = unittest.TextTestRunner(verbosity=2).run(suite)
    notebook_path = audit.HERE / "dataset_audit_AI_assisted.ipynb"
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
    notebook_ok = all(cell["execution_count"] is not None and not any(o["output_type"] == "error" for o in cell["outputs"]) for cell in code_cells)
    record = {
        "independent_validation": independent,
        "edge_cases": {"run": tests.testsRun, "failures": len(tests.failures), "errors": len(tests.errors)},
        "notebook": {"file": notebook_path.name, "code_cells": len(code_cells), "all_executed_without_errors": notebook_ok,
                     "sha256": hashlib.sha256(notebook_path.read_bytes()).hexdigest()},
    }
    audit.write_json(output / "validation_results.json", record)
    print(json.dumps(record, indent=2))
    return 0 if not independent["failed"] and tests.wasSuccessful() and notebook_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
