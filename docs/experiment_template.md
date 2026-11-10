# Individual experiment record

Copy to `results/experiments/<experiment-id>/record.md` for a run, adjusting the relative guide links below for that location. Record what changed; link shared details rather than repeating them. Use a commit-specific link or path plus commit identifier so later edits do not change the run's meaning.

- **ID, author, date, and question:**
- **Versions used:** code commit (and any uncommitted changes); [protocol](methodology.md), [data version/hashes](../data/README.md), and [environment](../src/README.md) at their recorded versions; shared configuration path if one exists.
- **Changes from that protocol/configuration:** exact feature group/columns, model, and settings. Link unchanged definitions; list all overrides, including seeds, split/folds, preparation, search space, tuning budget, and metrics where changed.
- **Run:** command or notebook path and execution order; link exact configuration/settings. Record anything needed to reproduce the run that the shared sources do not yet specify.
- **Results and outputs:** measured metrics with partition, units/aggregation, and paths under `results/experiments/<experiment-id>/`; note a failed or incomplete run explicitly.
- **Interpretation:** comparison with the baseline, limitations, deviations, and any external method/code attribution not already in the shared sources.

Before sharing, check that the linked records resolve the data version, dependencies, features, split, seeds, model/tuning settings, and metric definitions used. Shared comparison tables should be generated from these recorded results when the workflow is implemented. Do not fill gaps with assumed settings or fabricated values.
