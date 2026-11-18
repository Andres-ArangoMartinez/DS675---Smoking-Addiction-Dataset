# Dataset audit — AI-assisted reproduction

This folder reproduces the numerical and structural claims in
[dataset_description.md](../dataset_description.md). Its scientific findings are
preserved through the documentation updates. The work remains an individual descriptive analysis
rather than an integrated team protocol or model experiment.

The complementary [dataset provenance verifier](../../../../data/provenance_AI_assisted/README.md)
checks publisher metadata, source-file identity, and Git storage. This folder
provides the full statistical audit and conceptual explanations. Both use the
same common raw CSV; provenance records and executable checks are now available
in `data/provenance_AI_assisted/`.

Start with the executed [conceptual notebook](dataset_audit_AI_assisted.ipynb).
It explains each concept, formula, denominator, calculation, and interpretation
before displaying the results. The [generated report](results/audit_report_AI_assisted.md)
provides a readable summary. [audit.py](audit.py) contains the reusable calculations.

## Recorded reproduction

- **299/299 published numerical and structural claims match**, using exact counts
  and the precision of rounded values in the source. These are individual
  assertions, not 299 distinct statistical techniques.
- **323/323 independent checks passed in the recorded run**, recalculating from
  CSV strings with Python's standard-library `csv`, `statistics`, arithmetic,
  and keyed day lookups. This count includes the exact source-document hash;
  see the source-version explanation below.
- **Five edge-case tests pass**: shuffled rows/gaps/missing targets, duplicate keys,
  missing keys, a different input hash, and malformed CSV widths.
- **All 14 notebook code cells executed without errors**; all three figures were
  visually inspected during that audit. The source CSV remains unchanged.
  Recorded results retain the source-description fingerprint from that run.
- Input: **4,286,125 bytes**, SHA-256
  `7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907`.

The comparison expectations in [reference_values.json](reference_values.json)
were transcribed from the original document independently of the execution.
For example, a mean printed to three decimal places permits an absolute difference
of `0.0005`; the six-decimal target mean permits `0.0000005`. The files retain
full calculated precision. Qualitative assertions about source, license, clinical
validity, and data generation are outside this numerical comparison.

**Source versions and prior review.** 
The historical audit fingerprints the Spanish source at commit `3ed5900`, with
SHA-256 `22b299ed236c40024d40835a1fdc972f537a8fd39506b1352303da9b71b46e68`.
The current description is an English version with later documentary revisions,
so its byte fingerprint differs. Rechecking preserved historical results against
the current text passes **322/323 checks**; only `original_description_sha256`
differs. This is a source-version difference, not a numerical disagreement.
A fresh reproduction on November 18, 2026 passed **299/299 reference comparisons**
and **323/323 independent checks** using the current document fingerprint.
Historical outputs and reference expectations are preserved.

## Reproduce without replacing recorded results

Run the following commands from the repository root. The common CSV must already
exist at `data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv`; see
[data/README.md](../../../../data/README.md) for access and file verification.
The audit does not download, clean, impute, or overwrite the raw CSV.

The recorded environment uses Python 3.14.4; exact package versions are in
[requirements.txt](requirements.txt). If dependencies are needed, create a local
environment and use its interpreter for the subsequent commands:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r work/andres/02_dataset_description/dataset_audit_AI_assisted/requirements.txt
```

The audit script needs only NumPy and pandas beyond the standard library. Other
listed dependencies support the notebook, figures, and notebook execution.

### Fresh numerical reproduction

Export a new run to a separate review directory:

```powershell
python work/andres/02_dataset_description/dataset_audit_AI_assisted/audit.py --output tmp/dataset_audit_review
```

Choose an unused output directory for each run. Unlike the provenance verifier's
JSON output option, `audit.py --output` can overwrite files in an existing output
directory. Omitting `--output` writes into this folder's recorded `results/`.

Independently check the fresh report without invoking the validator's
result-writing entry point:

```powershell
@'
from pathlib import Path
import json
import sys

folder = Path("work/andres/02_dataset_description/dataset_audit_AI_assisted").resolve()
sys.path.insert(0, str(folder))
import audit
from validate_audit import independent_checks

result = independent_checks(audit.DEFAULT_CSV, Path("tmp/dataset_audit_review/audit_results.json"))
print(json.dumps(result, indent=2))
raise SystemExit(1 if result["failed"] else 0)
'@ | python -
```

Run the five existing edge-case tests without rewriting validation results:

```powershell
python -m unittest discover -s work/andres/02_dataset_description/dataset_audit_AI_assisted -p validate_audit.py -v
```

Exit codes for `audit.py`: `0` means all reference comparisons passed, `1` means
calculations completed with reference disagreements, and `2` means an input or
configuration issue prevented execution. A different raw hash is rejected by
default. To inspect an alternative CSV with the same schema, use a separate output:

```powershell
python work/andres/02_dataset_description/dataset_audit_AI_assisted/audit.py --csv 'path/to/alternative.csv' --allow-different-input --output tmp/alternative_audit
```

The expected values remain those of the reference CSV. An alternative-file run
does not execute the notebook, produce its figures, or change reference claims.

### Provenance and source comparison

Run the complementary verifier for local file identity, the bundled historical
metadata, and actual Git tracking/ignore behavior:

```powershell
python data/provenance_AI_assisted/verify.py
```

To retrieve the version-specific Kaggle archive, pinned GitHub CSV, and current
Kaggle metadata again:

```powershell
python data/provenance_AI_assisted/verify.py --online
```

The [verification guide](../../../../data/provenance_AI_assisted/README.md)
describes external-check status, optional JSON reports, and six separate
regression tests. Its [recorded online run](../../../../data/provenance_AI_assisted/results/verification_20261118.json)
passed 27 checks on November 18, 2026. Those assertions belong to the provenance
verifier and are separate from this audit's 299 reference comparisons and 323
independent checks.

### Recorded notebook and full regeneration

The executed notebook contains the conceptual explanations and saved figures.
The earlier editorial review also identified an obsolete audit-directory path in
its setup cell. That path is still present in the current notebook: **Run All
requires correcting `AUDIT_DIR` to the current location first**:

```python
AUDIT_DIR = ROOT / "work/andres/02_dataset_description/dataset_audit_AI_assisted"
```

The notebook is preserved unchanged in this documentation update. Use the
standalone reproduction commands above for the current checkout. After a future
setup correction, an intentional notebook rebuild will write this folder's
`results/`, including figures, and saving it will replace its execution outputs.

For a complete recorded-output rebuild, the full validator checks the default
paths, runs the five edge-case tests, inspects saved notebook execution, and
writes `results/validation_results.json`:

```powershell
python work/andres/02_dataset_description/dataset_audit_AI_assisted/validate_audit.py
```

This command includes the saved run's source-document fingerprint. Updating the
recorded source hash alone would not reproduce the audit; regenerate the complete
run only when intentionally replacing its artifacts. For a separate fresh run,
use the read-only independent check above.

## Conceptual map

| Reference | Concept and computation | Counting unit or denominator |
| --- | --- | --- |
| 1.1 / 1.9 | Byte size, SHA-256, Git blob identifier, logical CSV field counts | Raw bytes and logical CSV records |
| 1.2 | Row/column count, unique keys, exact day coverage, duplicate excess | Participant-days; separately unique participants |
| 1.3 / Annex A | Thematic groups, inferred types, observed ranges and categories | Columns and their observed cells |
| 1.4 | Stable profiles and category counts/percentages | One verified profile per participant |
| 1.5 | Daily categorical frequencies | Observed participant-days, with both total and observed denominators |
| 1.5–1.6 | Mean, median, minimum, maximum, sample variance/std, quartiles, IQR | Each numeric column's observed values |
| 1.6 | Target availability and interval frequencies | Availability: all rows; histogram: observed targets |
| 1.6.1 | Within-person distinct counts/std, person means, daily means | Observed target values in the relevant participant/day group |
| 1.6.1 | Pearson correlation, pooled and person-centered | Actual consecutive-day pairs with both target endpoints observed |
| 1.7 | Missing cells, incomplete rows, incomplete columns | All cells, all rows, or columns respectively |
| 1.7 | Scores, nonnegative fields, time syntax, binary categories | Observed cells eligible for each explicit rule |
| 1.7.1 | Five proposed cross-field semantic flags | Eligible rows stated separately for each check |
| Extension | Weighted between/within sum-of-squares partition | All observed target values, weighted by observed count per participant |

The original document does not name its thirteen nonnegative fields. This
implementation explicitly checks the thirteen nonscore numeric fields, including
`Day_Number`; see `NONNEGATIVE` in `audit.py`. This is a transparent operational
choice rather than a recovered specification from an undocumented earlier script.

## Important interpretation details

**Repeated observations.** There are 30,000 participant-days from 1,000 simulated
participants, rather than 30,000 independent people. Complete day keys can coexist
with incomplete measurements.

**Different denominators.** Missingness affects 4,982 / 1,050,000 cells (**0.474476%**)
but 4,630 / 30,000 rows (**15.433333%**). These values answer different questions.
The observed target count is 29,651; its 349 missing values remain missing.

**Sample dispersion.** For the target, mean = **5.994904**, median = **6.0**,
sample standard deviation = **1.684405**, Q1 = **4.8**, Q3 = **7.2**, and IQR =
**2.4**. `ddof=1` reproduces sample dispersion; it does not establish independence
or supply a standard error. Quartiles use linear interpolation. Numeric summaries
use each column's available measurements, not listwise deletion of incomplete rows.

**Temporal association.** There are 29,000 potential adjacent-day pairs and
28,338 complete pairs. Pooled lag-one Pearson correlation = **0.858927**, while
person-centered lag-one correlation = **−0.035083** on the same pairs. Person
means use all observed days before pair selection. The second coefficient is a
pooled correlation of deviations, not an average of individual autocorrelations.
It neither proves independence nor evaluates a forecasting model. Full-series
centering must not be copied into prospective features that use held-out days.

**Additional extension.** The weighted sum-of-squares partition attributes
**86.346560%** of observed target sum of squares to differences between observed
participant means. This descriptive share is not an ICC, causal effect, or model
performance measure. It adds a quantified illustration of the within/between
distinction without modifying the original audit.

**Type inference.** Pandas 3 natively infers nine text columns as `str`.
Explicitly requesting `object` for those nine columns reproduces the historical
20 `float64` / 6 `int64` / 9 `object` inventory. Native and historical dtypes are
both retained, with the policy disclosed rather than hiding the version difference.
See the [pandas string migration guide](https://pandas.pydata.org/docs/user_guide/migration-3-strings.html).

**Provenance boundaries.** The local CSV matches the initial audit's hash.
The complementary [source record](../../../../data/provenance_AI_assisted/sources.json)
pins the selected Kaggle version, public URLs, GitHub commit, and expected hashes.
The bundled [metadata snapshot](../../../../data/provenance_AI_assisted/evidence/kaggle_metadata_20261116.json)
records publisher statements about version and license. The provenance verifier
can repeat direct byte comparisons with both public CSV sources; offline runs
explicitly identify external checks that were not performed. These materials
provide reproducible evidence alongside the statistical audit. A matching hash
identifies content; it does not authenticate download origin. CC0 is attributed
to publisher metadata. The CSV does not establish a validated score formula or
data-generation mechanism.

## Output inventory

| File | Purpose |
| --- | --- |
| `results/audit_results.json` | Full-precision metrics, input/source hashes, versions, and calculation policies |
| `results/audit_report_AI_assisted.md` | Separate readable audit report |
| `results/reference_comparison.csv` / `.json` | All 299 expected/actual comparisons and tolerances |
| `results/inventory.csv` | Exhaustive 35-variable inventory, historical and native dtypes |
| `results/numeric_summary.csv` | All 26 numeric variables, observed N, location, dispersion, quartiles |
| `results/missing_by_column.csv` | All 35 column denominators and missingness values |
| `results/categorical_frequencies.csv` | Participant-profile and daily category frequencies with denominator labels |
| `results/target_histogram.csv` | Ten target bins with endpoint conventions and observed-value percentages |
| `results/participant_target_summary.csv` / `daily_target_summary.csv` | Individual and daily descriptive summaries |
| `results/rows_per_participant.csv` / `rows_per_day.csv` | Key-panel count evidence |
| `results/validity_checks.csv` / `semantic_checks.csv` | Explicit checks, flags, and eligible denominators |
| `results/adjacent_pairs.csv` | Recreated full pair evidence; excluded from Git to avoid a large derived data copy |
| `results/figures/*.png` | Three figures generated by the notebook |
| `results/validation_results.json` | Independent checks, edge cases, executed notebook state and hash |

The standalone script exports tables/report; the notebook additionally generates
figures. These are the default output paths; a fresh `audit.py --output` run uses
the selected directory instead. The common raw CSV is tracked, while ignore rules
apply to new raw/processed files as explained in [data/README.md](../../../../data/README.md).
This audit and the provenance verifier leave the raw dataset unchanged.
