# Dataset access and verified file

The selected source is **[Smoking Addiction Dataset, Kaggle version 1](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/versions/1)**. The bundled [Kaggle metadata snapshot](provenance_AI_assisted/evidence/kaggle_metadata_20261116.json), saved during the provenance work recorded on 2026-11-16, identifies dataset `11749711`, version 1 and reports a CC0: Public Domain license. Its source is the [official metadata endpoint](https://www.kaggle.com/api/v1/datasets/view/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset). The [source record and verification code](provenance_AI_assisted/README.md) reproduce the file, metadata, source-comparison, and Git-storage checks. CC0 is attributed to publisher metadata; it is not inferred from the CSV.

Keep the unchanged file at `data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv`. The verified file has **30,000 records, 35 columns, 1,000 participants, and days 1–30 per participant**, with no duplicate participant-day keys. There are **349 missing Overall_Craving_Score values**. The tracked [dataset description](../work/andres/02_dataset_description/dataset_description.md) and [AI-assisted schema and quality audit](../work/andres/02_dataset_description/dataset_audit_AI_assisted/README.md) document these measurements; the [full audit results](../work/andres/02_dataset_description/dataset_audit_AI_assisted/results/audit_results.json) identify the same input hash.

File size: **4,286,125 bytes**. SHA-256:

```text
7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907
```

The raw CSV has the recorded hash of the Kaggle version-1 CSV and the NumiKun copy at commit `aa3faf512362f941721a85793e65baf5c3c7d760`. Its Git blob identifier is `80bbba4a3289940698a2926618bf0f5f1525e69f`, matching the initial audit. The verifier's `--online` mode retrieves the version-specific Kaggle archive and pinned GitHub CSV and compares their bytes directly with the common raw file. An offline run checks the local file and bundled metadata, and explicitly marks external comparisons as not checked. The metadata snapshot records publisher claims; file identity does not validate the data-generation mechanism or model performance.

## Reproduce the verification

From the repository root, run the local checks with Python's standard library:

```powershell
python data/provenance_AI_assisted/verify.py
```

To retrieve the public sources again and compare them directly:

```powershell
python data/provenance_AI_assisted/verify.py --online --output tmp/provenance_check.json
```

Choose a new output filename for each saved run; existing reports are never overwritten. Downloads are compared in memory and the raw CSV is never replaced. The JSON report distinguishes passed, failed, unavailable, and unperformed checks. See the [verification guide](provenance_AI_assisted/README.md) for saved-file comparisons, exit codes, and tests.

For the complete descriptive measurements and their explanations, follow the [statistical audit reproduction instructions](../work/andres/02_dataset_description/dataset_audit_AI_assisted/README.md).

## Protocol and storage

The [proposed next-day learning objective](../work/andres/03_supervised_learning_objective/propouse_supervised_learning_objective.md) specifies the prediction horizon, information cutoff, and evaluation population. It remains an individual proposal, not a recorded group-approved protocol. Keep shared team protocol specifications in [methodology.md](../docs/methodology.md) and agreements in the [decision log](../docs/decisions.md).

Use this single raw copy in all analyses. `git ls-files -- data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv` confirms that the raw dataset is tracked. The current [.gitignore](../.gitignore) ignores new raw and processed files except `.gitkeep` markers; ignore rules do not untrack an already tracked file. The local `data/processed/next_day_protocol_v1.csv` is ignored and is not tracked. Preserve the raw CSV and share acquisition instructions, hashes, and audit code. The scientific protocol requires training-only fitted transformations for missing predictors; the proposed objective excludes invented target labels. These are protocol requirements, not evidence of a completed model experiment. No fitted-model or performance result is supplied by the descriptive audit.
