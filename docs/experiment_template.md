# Individual experiment record

Copy to `results/experiments/<experiment-id>/record.md` for a run. The shared-guide links below work from either location. Record what changed and the exact commit(s) used; guide links alone do not identify a run's versions.

- **ID, author, date, and question:**
- **Versions used:** code commit (and any uncommitted changes); [protocol](https://github.com/Andres-ArangoMartinez/DS675---Smoking-Addiction-Dataset/blob/main/docs/methodology.md), [data version/hashes](https://github.com/Andres-ArangoMartinez/DS675---Smoking-Addiction-Dataset/blob/main/data/README.md), and [environment](https://github.com/Andres-ArangoMartinez/DS675---Smoking-Addiction-Dataset/blob/main/src/README.md) from that commit, or record their commits if different; shared configuration path if one exists.
- **Changes from that protocol/configuration:** exact feature group/columns, model, and settings. Link unchanged definitions; list all overrides, including seeds, split/folds, preparation, search space, tuning budget, and metrics where changed.
- **Run:** command or notebook path and execution order; link exact configuration/settings. Record anything needed to reproduce the run that the shared sources do not yet specify.
- **Results and outputs:** measured metrics with partition, units/aggregation, and paths under `results/experiments/<experiment-id>/`; note a failed or incomplete run explicitly.
- **Interpretation:** comparison with the baseline, limitations, deviations, and any external method/code attribution not already in the shared sources.

Before sharing, check that the linked records resolve the data version, dependencies, features, split, seeds, model/tuning settings, and metric definitions used. Shared comparison tables should be generated from these recorded results when the workflow is implemented. Do not fill gaps with assumed settings or fabricated values.
