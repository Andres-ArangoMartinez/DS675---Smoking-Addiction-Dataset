# Dataset instructions

Source: [Smoking Addiction Dataset on Kaggle](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data). No data has been downloaded or fabricated by this setup.

## Obtain the same version

Before analysis, the team must choose a dataset version and fill in this record. Use that specific Kaggle version, not an unspecified latest download. Check the license and any Kaggle access requirements. Each teammate should download the agreed files once into `data/raw/` and compare filenames and hashes with the shared record. If a recorded version is unavailable, discuss a replacement and record the change rather than silently substituting it.

| Item | Agreed value |
| --- | --- |
| Kaggle version identifier and exact version link | Pending team agreement |
| Version/release date and acquisition date | Pending |
| Original data filenames | Pending |
| SHA-256 per file | Pending |
| License / reuse conditions | Pending verification |
| Schema and audited row/participant counts | Pending audit |
| Acquisition / extraction steps | Pending |

On Windows, calculate each downloaded file's hash in PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'data/raw/ACTUAL_FILENAME.csv'
```

Replace `ACTUAL_FILENAME.csv` with the real filename; this is an example command, not a claim that such a file exists.

## Preserve and recreate

- `raw/`: original downloaded data. Leave it unchanged. Do not edit cells, rename columns, or overwrite the original files during preparation.
- `processed/`: locally generated data. Future reviewed code in `src/` should recreate it from the agreed raw files, using documented commands, settings, and an environment record. No preparation command exists yet.
- Record quality checks, exclusions, and learned preprocessing in the methodology and each experiment. Fit learned transformations only on training data within the agreed validation procedure.
- Use this shared local data location from all notebooks and individual work folders; avoid duplicated datasets.

Both data directories are ignored except for `.gitkeep`. Instructions and version/hash metadata belong in Git. Do not upload data archives, credentials, or large temporary files; inspect GitHub Desktop's changed-file list before committing. The final environment and regeneration procedure must still be implemented and verified.
