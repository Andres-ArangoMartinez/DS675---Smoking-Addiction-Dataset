# Experiment record template

Copy this template to `results/experiments/<experiment-id>/record.md` when an experiment is actually undertaken. Give each experiment a unique ID and its own output location, for example `exp-001-baseline`. Do not treat this blank template as a completed run.

- Experiment ID: **pending**
- Status (planned / running / completed / failed): **pending**
- Question and comparison being tested: **pending**
- Author: **pending**
- Date (`YYYY-MM-DD`): **pending**
- Data version, source filenames, and SHA-256 hashes: **pending**
- Code version (commit identifier; also identify any uncommitted changes): **pending**
- Environment (OS, Python version, package versions, and environment file when implemented): **pending**
- Run command / notebook and execution order: **pending**
- Target, horizon, prediction cutoff, and evaluation population: **pending**
- Features (exact columns, lags/windows, group, availability rules): **pending**
- Preparation and exclusions, including how learned steps were fitted: **pending**
- Split and validation folds (participant rules, time boundaries, eligible cohort, counts, and overlap checks): **pending**
- Random seed(s), including split/search/model seeds or why a step is deterministic: **pending**
- Model settings, preprocessing settings, hyperparameter search, tuning budget, and selection rule: **pending**
- Metrics, aggregation/weighting, and uncertainty method: **pending**
- Output paths under `results/experiments/<experiment-id>/`: **pending**
- Findings and comparison with the baseline: **pending measured results**
- Limitations, failures, and deviations from the agreed protocol: **pending**
- External methods/code used, exact source/version, license, and adaptations: **pending**
- Reviewer and verification evidence: **pending actual review**

## Metric results (fill only after execution)

| Evaluation partition | Metric | Value | Units / aggregation | Evidence path |
| --- | --- | --- | --- | --- |
| Pending | Pending | Not measured | Pending | Pending |

Keep compact records and selected outputs in Git. Keep large or sensitive intermediate outputs local, with a documented retrieval or regeneration method. Shared comparison tables in `results/tables/` should be generated from these experiment records when the experimental workflow is implemented; avoid manually copying scores into competing tables.
