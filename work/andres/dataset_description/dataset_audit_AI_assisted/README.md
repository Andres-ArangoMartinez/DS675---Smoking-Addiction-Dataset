# Dataset audit — AI-assisted reproduction

This separate working folder reproduces the measurable claims in the original
[dataset_description.md](../dataset_description.md), which is preserved unchanged.
All code comments and notebook explanations are in English. The work remains an
individual analysis rather than an integrated team protocol or model experiment.

Start with the executed [conceptual notebook](dataset_audit_AI_assisted.ipynb).
It explains each concept, formula, denominator, calculation, and interpretation
before displaying the results. The [generated report](results/audit_report_AI_assisted.md)
provides a readable summary. [audit.py](audit.py) contains the reusable calculations.

## Verified reproduction

- **299/299 published numerical and structural claims match**, using exact counts
  and the precision of rounded values in the source. These are individual
  assertions, not 299 distinct statistical techniques.
- **323/323 independent checks pass**, recalculating from CSV strings with Python's
  standard-library `csv`, `statistics`, arithmetic, and keyed day lookups.
- **Five edge-case tests pass**: shuffled rows/gaps/missing targets, duplicate keys,
  missing keys, a different input hash, and malformed CSV widths.
- **All 14 notebook code cells executed without errors**; all three figures were
  visually inspected. The source CSV and original description remain unchanged.
- Input: **4,286,125 bytes**, SHA-256
  `7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907`.

The comparison expectations in [reference_values.json](reference_values.json)
were transcribed from the original document independently of the execution.
For example, a mean printed to three decimal places permits an absolute difference
of `0.0005`; the six-decimal target mean permits `0.0000005`. The files retain
full calculated precision. Qualitative assertions about source, license, clinical
validity, and data generation are outside this numerical comparison.

## Run from the repository root

The common raw CSV must already exist at
`data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv`; see
[data/README.md](../../../../data/README.md) for the project's acquisition
instructions. The audit does not download, clean, impute, or overwrite it.

The recorded environment uses Python 3.14.4; exact package versions are in
[requirements.txt](requirements.txt). Use a local environment if dependencies are
needed:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r work/andres/dataset_description/dataset_audit_AI_assisted/requirements.txt
```

With that interpreter or an environment containing those packages:

```powershell
python work/andres/dataset_description/dataset_audit_AI_assisted/audit.py
```

The audit script needs only NumPy and pandas beyond the Python standard library.
The remaining dependencies support the notebook, plots, and notebook execution.
Open `dataset_audit_AI_assisted.ipynb` with a Python kernel and **Run All** to
recreate the explained calculations and figures. The notebook can run from its
own folder or the repository root. To execute it programmatically from the root:

```powershell
@'
from pathlib import Path
import nbformat
from nbclient import NotebookClient

p = Path("work/andres/dataset_description/dataset_audit_AI_assisted/dataset_audit_AI_assisted.ipynb")
nb = nbformat.read(p, as_version=4)
NotebookClient(nb, timeout=180, kernel_name="python3", resources={"metadata": {"path": str(p.parent.resolve())}}).execute()
nbformat.write(nb, p)
'@ | python -
```

After executing the notebook, independently validate the exported results:

```powershell
python work/andres/dataset_description/dataset_audit_AI_assisted/validate_audit.py
```

Exit codes for `audit.py`: `0` means all reference comparisons passed, `1` means
calculations completed with reference disagreements, and `2` means input/configuration
prevented execution. A different raw hash is rejected by default. To deliberately
audit an alternative with the same schema, preserve the reference results by
choosing a separate output directory:

```powershell
python work/andres/dataset_description/dataset_audit_AI_assisted/audit.py --csv 'path/to/alternative.csv' --allow-different-input --output 'tmp/alternative_audit'
```

`validate_audit.py` validates the recorded reference run at the default paths.
Notebook results and its strict reproduction assertions also target the reference
CSV. An alternative-file CLI run does not automatically execute that notebook or
produce its figures. No source claims or expected values are rewritten to make an
alternative pass.

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

**Provenance boundaries.** The local CSV matches the initial audit's hash. That
does not independently establish its download origin or license. Other project
documents mention later provenance work, but some linked artifacts are absent
from this checkout. This work neither recreates those claims nor edits them.
The CSV does not establish a validated score formula or data-generation mechanism.

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
figures. Raw and processed project data stay under the existing common data policy.
No commit or publication is part of this work.
