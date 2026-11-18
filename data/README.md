# Dataset access and verified file

The experimental CSV has been downloaded from **[Smoking Addiction Dataset, Kaggle version 1](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/versions/1)**. The [official metadata](https://www.kaggle.com/api/v1/datasets/view/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset) identifies dataset `11749711`, version 1 and a CC0: Public Domain license. The selected Kaggle notebook uses input-version ID `19129285`.

Keep the unchanged file at `data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv`. The verified file has **30,000 records, 35 columns, 1,000 participants, and days 1–30 per participant**, with no duplicate participant-day keys. There are **349 missing Overall_Craving_Score values**. The exact [schema and quality audit](../work/andres/predictive_protocol/dataset_audit.json) were calculated from this file.

File size: **4,286,125 bytes**. SHA-256:

```text
7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907
```

The Kaggle file is byte-identical to the CSV at NumiKun commit `aa3faf512362f941721a85793e65baf5c3c7d760`; see the [provenance record](../work/andres/predictive_protocol/baseline_provenance.json). This verifies file identity, not model performance or the data-generation mechanism.

## Download and recreate

From the repository root in PowerShell:

```powershell
New-Item -ItemType Directory -Path 'tmp/data_download' -Force | Out-Null
Invoke-WebRequest -Uri 'https://www.kaggle.com/api/v1/datasets/download/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset?datasetVersionNumber=1' -OutFile 'tmp/data_download/kaggle_v1.zip'
Expand-Archive -LiteralPath 'tmp/data_download/kaggle_v1.zip' -DestinationPath 'data/raw'
Get-FileHash -Algorithm SHA256 -LiteralPath 'data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv'
python work/andres/predictive_protocol/prepare.py --export
```

For an already populated `data/raw/`, compare hashes and preserve the existing original rather than overwriting it. The preparation script refuses a CSV with a different hash. It recreates audit/configuration files and `data/processed/next_day_protocol_v1.csv`; it does not fit models.

## Protocol and storage

The [concrete next-day proposal](../work/andres/predictive_protocol/README.md) fixes the feature columns, three initial days, three-day history and target-day partitions. Its [temporal checks](../work/andres/predictive_protocol/temporal_validation.json) have passed. Keep shared team protocol decisions in [methodology.md](../docs/methodology.md).

Use this single raw copy in all analyses. Raw and processed files remain excluded from Git; share the acquisition instructions, hashes, audit, and preparation code. Missing predictors will be processed using training-only fitted transformations; missing target labels are never imputed. No fitted-model or performance result is supplied by this data-preparation step.
