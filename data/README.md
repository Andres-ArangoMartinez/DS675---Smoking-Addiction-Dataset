# Dataset instructions

Source: [Smoking Addiction Dataset on Kaggle](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data). The [Milestone 2 proposal](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf) describes synthetic longitudinal data with 1,000 participants observed over 30 days, 30,000 records, and 35 columns. Verify those reported characteristics against the selected download, including feature types and target meaning, before analysis.

## Obtain the same version

Choose a Kaggle version together and record it below. Each teammate should obtain that exact version, check access/license conditions, and place the unchanged files in `data/raw/`. Compare filenames and hashes; discuss any replacement version rather than silently substituting it.

| Shared data record | Value to complete after selection/audit |
| --- | --- |
| Kaggle version identifier/link and release/acquisition dates | Not recorded |
| Original filenames and SHA-256 per file | Not recorded |
| License / reuse conditions | Not verified |
| Audited schema, feature types, row/participant counts, quality findings, and exclusions | Not recorded |
| Acquisition / extraction steps | Not recorded |

On Windows, calculate each downloaded file's hash in PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'data/raw/ACTUAL_FILENAME.csv'
```

Replace `ACTUAL_FILENAME.csv` with the downloaded filename.

## Preserve and recreate

- `raw/`: unchanged original files; use this one local copy from all analyses.
- `processed/`: generated data, recreated by shared code in `src/`. Document the preparation command and dependencies there when implemented.
- Follow the checks and training-only preparation rules in [methodology.md](../docs/methodology.md#data-and-preparation).

The data folders are ignored except for `.gitkeep`. Track these instructions and metadata, not datasets or archives. See [results/README.md](../results/README.md) for output storage. Data acquisition and processed-data regeneration still need implementation and verification.
