"""Reproduce the descriptive audit without changing or imputing the source CSV.

Run from any directory. Paths default to this repository's common raw dataset.
The adjacent reference_values.json contains claims transcribed from the original
dataset_description.md, not values learned from the current execution.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import platform
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEFAULT_CSV = ROOT / "data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv"
ORIGINAL = HERE.parent / "dataset_description.md"
REFERENCE = HERE / "reference_values.json"
EXPECTED_SHA256 = "7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907"
TARGET = "Overall_Craving_Score"
KEYS = ["Participant_ID", "Day_Number"]
PROFILE = ["Age_Group", "Gender", "Occupation_Status", "Nicotine_Use_Duration_Months"]
DEMOGRAPHICS = PROFILE[:3]
BINARY = ["Attempted_To_Resist_Craving", "Successfully_Resisted", "Major_Stress_Event_Today"]
GROUPS = {
    "Identification": KEYS,
    "Demographics": DEMOGRAPHICS,
    "Nicotine and craving": [
        "Nicotine_Use_Duration_Months", "Pouches_Per_Day", "Pouch_Strength_mg",
        "First_Pouch_Time", "Time_Since_Last_Pouch_Minutes",
        "Longest_Nicotine_Free_Period_Hours", "Morning_Cravings_Score",
        "Afternoon_Cravings_Score", "Evening_Cravings_Score", TARGET,
        "Craving_Triggers", "Craving_Intensity_Peak", "Craving_Duration_Minutes",
        "Attempted_To_Resist_Craving", "Successfully_Resisted",
    ],
    "Psychology": [
        "Daily_Anxiety_Score", "Morning_Anxiety_Score", "Evening_Anxiety_Score",
        "Perceived_Stress_Score", "Mood_Score", "Irritability_Score", "Restlessness_Score",
    ],
    "Habits and activities": [
        "Sleep_Duration_Hours", "Sleep_Quality_Score", "Caffeine_Intake_mg",
        "Exercise_Minutes", "Screen_Time_Hours", "Work_Or_Study_Hours",
        "Major_Stress_Event_Today", "Social_Interaction_Hours",
    ],
}
EXPECTED_COLUMNS = [column for columns in GROUPS.values() for column in columns]
TEXT_COLUMNS = KEYS[:1] + DEMOGRAPHICS + ["First_Pouch_Time", "Craving_Triggers"] + BINARY
SCORES = [c for c in EXPECTED_COLUMNS if c.endswith("_Score")] + ["Craving_Intensity_Peak"]
# The original names 13 nonnegative checks without enumerating their columns.
# Operationalize them as the 13 numeric fields outside the score-field list.
NONNEGATIVE = [
    "Day_Number", "Nicotine_Use_Duration_Months", "Pouches_Per_Day", "Pouch_Strength_mg",
    "Time_Since_Last_Pouch_Minutes", "Longest_Nicotine_Free_Period_Hours",
    "Craving_Duration_Minutes", "Sleep_Duration_Hours", "Caffeine_Intake_mg",
    "Exercise_Minutes", "Screen_Time_Hours", "Work_Or_Study_Hours",
    "Social_Interaction_Hours",
]


def plain(value: Any) -> Any:
    """Convert pandas/numpy values into strict JSON (no NaN or Infinity)."""
    if isinstance(value, dict):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(v) for v in value]
    if isinstance(value, np.generic):
        value = value.item()
    if value is pd.NA or (isinstance(value, float) and not math.isfinite(value)):
        return None
    return value


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(plain(value), indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def inspect_csv(raw: bytes) -> dict:
    """Check logical CSV records before pandas can normalize row widths."""
    reader = csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline=""), strict=True)
    header = next(reader)
    widths = Counter()
    malformed = []
    empty_cells = 0
    for record_number, fields in enumerate(reader, start=2):
        widths[len(fields)] += 1
        empty_cells += sum(field == "" for field in fields)
        if len(fields) != len(header):
            malformed.append({"csv_record": record_number, "fields": len(fields)})
    return {
        "header": header, "header_fields": len(header),
        "duplicate_header_names": [k for k, n in Counter(header).items() if n > 1],
        "data_records": sum(widths.values()), "field_count_frequencies": dict(widths),
        "malformed_records": len(malformed), "malformed_examples": malformed[:10],
        "literal_empty_cells": empty_cells,
    }


def load_data(path: Path, *, allow_different_input: bool = False) -> tuple[pd.DataFrame, dict]:
    """Read one byte snapshot, preserving the raw file and historical dtypes."""
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256 and not allow_different_input:
        raise ValueError("CSV hash differs from the audited reference. Use --allow-different-input to audit an intentional alternative.")
    syntax = inspect_csv(raw)
    if syntax["malformed_records"] or syntax["duplicate_header_names"]:
        raise ValueError(f"CSV structure is ambiguous: {syntax}")
    missing = sorted(set(EXPECTED_COLUMNS) - set(syntax["header"]))
    extra = sorted(set(syntax["header"]) - set(EXPECTED_COLUMNS))
    if missing or extra:
        raise ValueError(f"Unexpected schema. Missing={missing}; extra={extra}")
    # The native read records the behavior of the installed pandas version.
    native = pd.read_csv(io.BytesIO(raw), encoding="utf-8-sig")
    # Explicit object text columns reproduce the original pre-pandas-3 report.
    # Numeric dtypes are still inferred; no measurements are coerced or imputed.
    df = pd.read_csv(io.BytesIO(raw), encoding="utf-8-sig", dtype={c: object for c in TEXT_COLUMNS})
    numeric_columns = [c for c in EXPECTED_COLUMNS if c not in TEXT_COLUMNS]
    invalid = [c for c in numeric_columns if not pd.api.types.is_numeric_dtype(df[c])]
    if invalid:
        raise ValueError(f"Expected numeric columns contain nonnumeric values: {invalid}")
    if len(df) == 0:
        raise ValueError("The dataset has no observations.")
    if any(np.isinf(df[c].to_numpy(dtype=float)).any() for c in numeric_columns):
        raise ValueError("Infinite numeric values are not supported by this audit.")
    metadata = {
        "provenance": {
            "file_name": path.name, "size_bytes": len(raw), "sha256": digest,
            "git_blob_sha1": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(),
            "matches_reference_sha256": digest == EXPECTED_SHA256,
            "reference_document_sha256": hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
            "audit_code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "reference_values_sha256": hashlib.sha256(REFERENCE.read_bytes()).hexdigest(),
            "source_claim_scope": "Byte identity verified locally; origin, license, and generator are not established by this calculation.",
        },
        "environment": {"python": platform.python_version(), "pandas": pd.__version__, "numpy": np.__version__},
        "reading_policy": {
            "encoding": "utf-8-sig", "missing_values": "pandas default NA tokens; raw empty strings also counted separately",
            "text_types": "Explicit object dtype for the nine known text columns; numeric types inferred",
            "std_ddof": 1, "quantile_interpolation": "linear", "imputation": "none",
            "native_dtype_counts": native.dtypes.astype(str).value_counts().to_dict(),
            "audit_dtype_counts": df.dtypes.astype(str).value_counts().to_dict(),
            "native_dtypes": native.dtypes.astype(str).to_dict(),
        },
        "csv_syntax": syntax,
    }
    return df, metadata


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Use available values in each column, with sample variance/std (ddof=1)."""
    records = []
    for column in df.select_dtypes(include="number"):
        s = df[column].dropna()
        q1, q3 = s.quantile([0.25, 0.75], interpolation="linear")
        records.append({
            "column": column, "observed": len(s), "missing": int(df[column].isna().sum()),
            "min": s.min(), "max": s.max(), "mean": s.mean(), "median": s.median(),
            "sample_variance": s.var(ddof=1), "sample_std": s.std(ddof=1),
            "q1": q1, "q3": q3, "iqr": q3 - q1,
        })
    return pd.DataFrame(records).set_index("column")


def frequency_table(series: pd.Series, variable: str, unit: str) -> list[dict]:
    """Report both denominators; missing cells are not a category."""
    counts = series.dropna().value_counts().sort_index()
    return [{
        "variable": variable, "category": str(category), "unit": unit, "count": int(count),
        "observed_denominator": int(series.notna().sum()), "total_denominator": len(series),
        "percent_observed": 100 * count / series.notna().sum(), "percent_total": 100 * count / len(series),
    } for category, count in counts.items()]


def longitudinal_summary(df: pd.DataFrame) -> tuple[dict, dict[str, pd.DataFrame]]:
    """Use only actual (t, t+1) pairs and never bridge a missing day/value."""
    if df[KEYS].isna().any().any() or df.duplicated(KEYS).any():
        return {"status": "not_computed: missing or duplicate participant-day keys"}, {}
    ordered = df.sort_values(KEYS).copy()
    grouped = ordered.groupby("Participant_ID", sort=True)
    person = grouped[TARGET].agg(observed="count", distinct="nunique", mean="mean", sample_std="std")
    daily = ordered.groupby("Day_Number")[TARGET].agg(observed="count", mean="mean", sample_std="std")
    # Full observed participant means are used for this descriptive calculation.
    # They must not be reused as forecasting features across a held-out period.
    ordered["participant_mean"] = grouped[TARGET].transform("mean")
    ordered["deviation"] = ordered[TARGET] - ordered["participant_mean"]
    grouped = ordered.groupby("Participant_ID", sort=True)
    ordered["next_day"] = grouped["Day_Number"].shift(-1)
    ordered["next_value"] = grouped[TARGET].shift(-1)
    ordered["next_deviation"] = grouped["deviation"].shift(-1)
    adjacent = ordered["next_day"].eq(ordered["Day_Number"] + 1)
    valid = adjacent & ordered[TARGET].notna() & ordered["next_value"].notna()
    pairs = ordered.loc[valid, [*KEYS, TARGET, "next_day", "next_value", "deviation", "next_deviation"]].copy()
    pooled_r = pairs[TARGET].corr(pairs["next_value"], method="pearson")
    centered_r = pairs["deviation"].corr(pairs["next_deviation"], method="pearson")
    # Exact sum-of-squares partition, using observed-count-weighted person means.
    observed = ordered[TARGET].notna()
    grand_mean = ordered.loc[observed, TARGET].mean()
    total_ss = ((ordered.loc[observed, TARGET] - grand_mean) ** 2).sum()
    within_ss = (ordered.loc[observed, "deviation"] ** 2).sum()
    between_ss = (person["observed"] * (person["mean"] - grand_mean) ** 2).sum()
    result = {
        "status": "computed", "participants_with_variation": int(person["distinct"].gt(1).sum()),
        "observations_per_person_min": int(person["observed"].min()),
        "observations_per_person_max": int(person["observed"].max()),
        "person_mean_min": person["mean"].min(), "person_mean_max": person["mean"].max(),
        "daily_mean_min": daily["mean"].min(), "daily_mean_max": daily["mean"].max(),
        "potential_adjacent_pairs": int(adjacent.sum()), "valid_adjacent_pairs": len(pairs),
        "pairs_excluded_for_missing_values": int(adjacent.sum() - len(pairs)),
        "pooled_lag1_pearson": pooled_r, "person_centered_lag1_pearson": centered_r,
        "centering_policy": "Subtract each participant's mean of all observed target values before selecting complete consecutive-day pairs.",
        "sum_of_squares": {
            "total": total_ss, "within": within_ss, "between": between_ss,
            "decomposition_residual": total_ss - within_ss - between_ss,
            "between_share": between_ss / total_ss if total_ss else None,
            "interpretation": "Descriptive weighted sum-of-squares share, not an ICC or causal fraction.",
        },
    }
    return plain(result), {"participant_target_summary": person, "daily_target_summary": daily, "adjacent_pairs": pairs}


def run_audit(df: pd.DataFrame, metadata: dict) -> tuple[dict, dict[str, pd.DataFrame]]:
    """Calculate all machine-verifiable claims and retain useful evidence tables."""
    n, p = df.shape
    grouped = df.groupby("Participant_ID", sort=True)
    per_person = grouped.size()
    per_day = df.groupby("Day_Number").size()
    profile_distinct = grouped[PROFILE].nunique(dropna=False)
    inconsistent = profile_distinct.gt(1)
    keys_complete = not df[KEYS].isna().any().any()
    day_sets_ok = grouped["Day_Number"].apply(lambda s: set(s) == set(range(1, 31)))
    structure = {
        "rows": n, "columns": p, "participants": df["Participant_ID"].nunique(),
        "distinct_days": df["Day_Number"].nunique(), "day_min": df["Day_Number"].min(), "day_max": df["Day_Number"].max(),
        "rows_per_person_min": per_person.min(), "rows_per_person_max": per_person.max(),
        "rows_per_day_min": per_day.min(), "rows_per_day_max": per_day.max(),
        "duplicate_keys_excess": int(df.duplicated(KEYS, keep="first").sum()),
        "rows_in_duplicate_keys": int(df.duplicated(KEYS, keep=False).sum()),
        "duplicate_rows_excess": int(df.duplicated(keep="first").sum()),
        "missing_key_cells": int(df[KEYS].isna().sum().sum()),
        "participants_with_profile_changes": int(inconsistent.any(axis=1).sum()),
        "profile_changes_by_column": inconsistent.sum().to_dict(),
        "participants_without_exact_days_1_to_30": int((~day_sets_ok).sum()),
        "balanced_keys_days_1_to_30": bool(keys_complete and not df.duplicated(KEYS).any() and day_sets_ok.all()),
        "group_column_counts": {k: len(v) for k, v in GROUPS.items()},
    }
    numeric = numeric_summary(df)
    missing_counts = df.isna().sum()
    missing_table = pd.DataFrame({"missing": missing_counts, "observed": n - missing_counts, "percent_rows": 100 * missing_counts / n})
    row_missing = df.isna().sum(axis=1)
    missingness = {
        "total_cells": n * p, "missing_cells": int(missing_counts.sum()),
        "missing_cell_percent": 100 * missing_counts.sum() / (n * p),
        "rows_with_missing": int(row_missing.gt(0).sum()), "rows_with_missing_percent": 100 * row_missing.gt(0).mean(),
        "complete_columns": int(missing_counts.eq(0).sum()), "incomplete_columns": int(missing_counts.gt(0).sum()),
        "incomplete_column_percent_min": missing_table.loc[missing_counts.gt(0), "percent_rows"].min(),
        "incomplete_column_percent_max": missing_table.loc[missing_counts.gt(0), "percent_rows"].max(),
        "by_column": missing_table.to_dict(orient="index"),
        "rows_by_number_missing": row_missing.value_counts().sort_index().to_dict(),
    }
    inventory = []
    group_for = {column: group for group, columns in GROUPS.items() for column in columns}
    for column in df:
        is_numeric = pd.api.types.is_numeric_dtype(df[column])
        inventory.append({
            "column": column, "group": group_for[column], "dtype": str(df[column].dtype),
            "native_dtype": metadata["reading_policy"]["native_dtypes"][column],
            "observed": int(df[column].notna().sum()), "missing": int(missing_counts[column]),
            "unique_observed": int(df[column].nunique()),
            "min": df[column].min() if is_numeric else None, "max": df[column].max() if is_numeric else None,
            "categories": sorted(df[column].dropna().unique().tolist()) if column in TEXT_COLUMNS and column != "Participant_ID" else None,
        })
    # A profile is counted once only after verifying its invariance. Conflicting
    # profiles are not silently resolved by selecting an arbitrary first row.
    profile_available = keys_complete and not inconsistent.any().any()
    frequency_rows = []
    if profile_available:
        profiles = df.drop_duplicates("Participant_ID")
        for column in DEMOGRAPHICS:
            frequency_rows.extend(frequency_table(profiles[column], column, "participant"))
    for column in ["Craving_Triggers", "First_Pouch_Time", *BINARY]:
        frequency_rows.extend(frequency_table(df[column], column, "participant-day"))
    frequencies = pd.DataFrame(frequency_rows)
    categories = {column: dict(zip(part["category"], part["count"])) for column, part in frequencies.groupby("variable")}
    histogram_counts, _ = np.histogram(df[TARGET].dropna(), bins=np.arange(11))
    histogram = pd.DataFrame({
        "interval": [f"[{i}, {i+1}{']' if i == 9 else ')'}" for i in range(10)],
        "count": histogram_counts, "percent_observed": 100 * histogram_counts / df[TARGET].notna().sum(),
    })
    target = numeric.loc[TARGET].to_dict()
    target["observed_percent"] = 100 * df[TARGET].notna().mean()
    target["missing_percent"] = 100 * df[TARGET].isna().mean()
    target["histogram_counts"] = histogram_counts.tolist()
    target["histogram_denominator"] = int(df[TARGET].notna().sum())
    target["histogram_values_outside_0_to_10"] = int((df[TARGET].notna() & ~df[TARGET].between(0, 10)).sum())
    checks = []
    for column in SCORES:
        checks.append({"rule": "score_in_0_to_10", "column": column, "eligible": int(df[column].notna().sum()), "flagged": int((df[column].notna() & ~df[column].between(0, 10)).sum())})
    for column in NONNEGATIVE:
        checks.append({"rule": "nonnegative", "column": column, "eligible": int(df[column].notna().sum()), "flagged": int(df[column].lt(0).sum())})
    time = df["First_Pouch_Time"]
    checks.append({"rule": "HH:MM", "column": "First_Pouch_Time", "eligible": int(time.notna().sum()), "flagged": int((time.notna() & ~time.str.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", na=False)).sum())})
    for column in BINARY:
        checks.append({"rule": "Yes_or_No", "column": column, "eligible": int(df[column].notna().sum()), "flagged": int((df[column].notna() & ~df[column].isin(["Yes", "No"])).sum())})
    validity = {"rules": checks, "score_fields_checked": len(SCORES), "nonnegative_fields_checked": len(NONNEGATIVE), "total_rule_violations": sum(c["flagged"] for c in checks)}
    zero_pouches = df["Pouches_Per_Day"].eq(0)
    comparable_peak = df[[TARGET, "Craving_Intensity_Peak"]].notna().all(axis=1)
    comparable_resistance = df[["Successfully_Resisted", "Attempted_To_Resist_Craving"]].notna().all(axis=1)
    components_present = df[["Morning_Cravings_Score", "Afternoon_Cravings_Score", "Evening_Cravings_Score"]].notna().all(axis=1)
    semantic = {
        "zero_pouches_with_first_time": {"count": int((zero_pouches & time.notna()).sum()), "eligible": int(zero_pouches.sum())},
        "zero_pouches_with_time_since_last": {"count": int((zero_pouches & df["Time_Since_Last_Pouch_Minutes"].notna()).sum()), "eligible": int(zero_pouches.sum())},
        "overall_above_peak": {"count": int((comparable_peak & df[TARGET].gt(df["Craving_Intensity_Peak"])).sum()), "eligible": int(comparable_peak.sum())},
        "success_without_attempt": {"count": int((df["Successfully_Resisted"].eq("Yes") & df["Attempted_To_Resist_Craving"].eq("No")).sum()), "eligible": int(comparable_resistance.sum())},
        "missing_overall_with_complete_components": {"count": int((df[TARGET].isna() & components_present).sum()), "eligible": int(df[TARGET].isna().sum())},
    }
    for record in semantic.values():
        record["percent_eligible"] = 100 * record["count"] / record["eligible"] if record["eligible"] else None
    longitudinal, temporal_tables = longitudinal_summary(df)
    report = plain({
        **metadata, "structure": structure, "inventory": {r["column"]: r for r in inventory},
        "numeric": numeric.to_dict(orient="index"), "missingness": missingness,
        "profile_frequencies_available": profile_available, "categorical_counts": categories,
        "target": target, "longitudinal": longitudinal, "validity": validity, "semantic": semantic,
    })
    tables = {
        "inventory": pd.DataFrame(inventory).set_index("column"), "numeric_summary": numeric,
        "missing_by_column": missing_table.rename_axis("column"),
        "categorical_frequencies": frequencies, "target_histogram": histogram,
        "validity_checks": pd.DataFrame(checks),
        "semantic_checks": pd.DataFrame.from_dict(semantic, orient="index").rename_axis("check"),
        "rows_per_participant": per_person.rename("rows").to_frame(), "rows_per_day": per_day.rename("rows").to_frame(),
        **temporal_tables,
    }
    return report, tables


def compare_reference(report: dict, reference_path: Path = REFERENCE) -> pd.DataFrame:
    """Compare independent reference claims using their published precision."""
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    rows = []
    for claim in reference["claims"]:
        actual: Any = report
        try:
            for key in claim["path"]:
                actual = actual[key]
        except (KeyError, IndexError, TypeError):
            actual = None
        expected, tolerance = claim["expected"], claim.get("absolute_tolerance", 0)
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            passed = isinstance(actual, (int, float)) and not isinstance(actual, bool) and math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance)
        else:
            passed = actual == expected
        rows.append({"section": claim["section"], "metric": ".".join(map(str, claim["path"])), "expected": expected, "actual": actual, "absolute_tolerance": tolerance, "passed": passed})
    return pd.DataFrame(rows)


def markdown_table(frame: pd.DataFrame) -> str:
    """Render small Markdown tables without requiring the optional tabulate package."""
    def cell(value: Any) -> str:
        value = plain(value)
        if value is None:
            return "—"
        if isinstance(value, float):
            return f"{value:.6f}"
        return str(value).replace("|", "\\|").replace("\n", " ")
    lines = ["| " + " | ".join(map(str, frame.columns)) + " |", "| " + " | ".join(["---"] * len(frame.columns)) + " |"]
    lines.extend("| " + " | ".join(cell(v) for v in row) + " |" for row in frame.itertuples(index=False, name=None))
    return "\n".join(lines)


def save_results(report: dict, tables: dict[str, pd.DataFrame], comparison: pd.DataFrame, output: Path) -> None:
    """Export deterministic, inspectable calculations and reference comparisons."""
    output.mkdir(parents=True, exist_ok=True)
    report["reference_comparison"] = {
        "claims_checked": len(comparison), "passed": int(comparison["passed"].sum()),
        "failed": int((~comparison["passed"]).sum()),
        "policy": "Exact counts and strings; half the last published decimal unit for rounded statistics.",
    }
    write_json(output / "audit_results.json", report)
    write_json(output / "reference_comparison.json", comparison.to_dict(orient="records"))
    comparison.to_csv(output / "reference_comparison.csv", index=False, lineterminator="\n")
    for name, table in tables.items():
        # The pairs table is evidence for the temporal calculation, not model input.
        table.to_csv(output / f"{name}.csv", index=not isinstance(table.index, pd.RangeIndex), lineterminator="\n")
    failed = comparison.loc[~comparison["passed"]]
    summary = report["reference_comparison"]
    lines = [
        "# Dataset audit — AI-assisted reproduction", "",
        "The original [dataset_description.md](../../dataset_description.md) is preserved. Results below are computed from the common raw CSV.", "",
        f"Reference claims: **{summary['passed']}/{summary['claims_checked']} passed**; **{summary['failed']} failed**.", "",
        f"CSV SHA-256: `{report['provenance']['sha256']}`.", "",
        "## Structure and missingness", "",
        markdown_table(pd.DataFrame([{"metric": k, "value": v} for k, v in report["structure"].items() if not isinstance(v, dict)])), "",
        markdown_table(tables["missing_by_column"].reset_index()), "",
        "## Numeric measurements", "", markdown_table(tables["numeric_summary"].reset_index()), "",
        "Each column uses its own observed values. Standard deviation and variance use ddof=1; quartiles use linear interpolation.", "",
        "## Categorical frequencies", "", markdown_table(tables["categorical_frequencies"]), "",
        "Demographics count participants once after checking profile invariance. Other frequencies count participant-days. Missing cells are excluded from the observed denominator.", "",
        "## Target distribution", "", markdown_table(tables["target_histogram"]), "",
        "Bins are left-closed/right-open, except [9, 10], which includes 10. Percentages divide by the observed target count.", "",
        "## Longitudinal description", "",
        markdown_table(pd.DataFrame([{"metric": k, "value": v} for k, v in report["longitudinal"].items() if not isinstance(v, dict)])), "",
        "Only actual consecutive days with both target values observed contribute to correlations. Centering uses each participant's full observed mean for description, not forecasting.", "",
        "Additional conceptual extension (not an original reference claim): weighted between/within sums of squares.", "",
        markdown_table(pd.DataFrame([{"metric": k, "value": v} for k, v in report["longitudinal"].get("sum_of_squares", {}).items()])), "",
        "## Syntactic and range checks", "", markdown_table(tables["validity_checks"]), "",
        "## Semantic flags", "", markdown_table(tables["semantic_checks"].reset_index()), "",
        "These flags require field definitions; they do not automatically establish data errors or justify reconstructing missing targets.", "",
        "## Types and reproducibility", "",
        f"Environment: {report['environment']}. Native dtypes: {report['reading_policy']['native_dtype_counts']}. Audit dtypes: {report['reading_policy']['audit_dtype_counts']}.", "",
        "The explicit object dtype for text columns reproduces the historical audit. This differs from pandas 3's default str inference without changing numeric measurements.", "",
        "## Reference disagreements", "",
        "No numerical disagreements at the precision published in the reference." if failed.empty else markdown_table(failed), "",
        "## Interpretation limits", "",
        "CSV calculations establish structure and descriptive values. Synthetic status, instrument validity, generator rules, license, and clinical or causal validity require external documentation. Hash identity does not establish origin. Missingness percentages do not establish MCAR/MAR/MNAR. Correlations do not establish independence or predictive performance.", "",
        "Full per-variable inventory, participant summaries, day summaries, pair evidence, and comparisons are provided in adjacent CSV/JSON files. See the notebook for the concepts and explicit calculation steps.", "",
    ]
    (output / "audit_report_AI_assisted.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--output", type=Path, default=HERE / "results")
    parser.add_argument("--allow-different-input", action="store_true", help="Audit a deliberately different file and report reference disagreements.")
    args = parser.parse_args()
    try:
        df, metadata = load_data(args.csv, allow_different_input=args.allow_different_input)
        report, tables = run_audit(df, metadata)
        comparison = compare_reference(report)
        save_results(report, tables, comparison, args.output)
    except (ValueError, OSError, csv.Error, UnicodeError) as error:
        parser.exit(2, f"Audit stopped: {error}\n")
    failed = int((~comparison["passed"]).sum())
    print(f"Audit complete: {len(comparison) - failed}/{len(comparison)} reference claims matched.")
    print(f"Results: {args.output.resolve()}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
