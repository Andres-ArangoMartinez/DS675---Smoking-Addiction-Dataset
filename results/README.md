# Recorded outputs

No experiments or scientific results exist from this setup. Use:

- `experiments/<experiment-id>/`: one location per experiment, beginning with a copy of the [experiment record template](../docs/experiment_template.md) named `record.md`. Keep the run's settings, metrics, selected outputs, and findings together.
- `tables/`: shared comparison tables generated from experiment records when the workflow is implemented.
- `figures/`: selected figures for analysis, the report, or presentation, with a traceable experiment source.

Track compact Markdown/JSON experiment records, small metric CSVs, and selected figures/tables after review. Record units, aggregation, data/code versions, and regeneration commands. Do not invent metric values or manually maintain competing score tables.

Large predictions, fitted model files, caches, raw data copies, videos, and temporary outputs should stay out of Git. The ignore rules cover common formats and `scratch/` or `cache/` folders, but cannot detect every large file: inspect file sizes and changed files before committing. Agree on an external storage/retrieval method if a large artifact must be shared, and document its hash and location in the experiment record.

LaTeX can reference selected figures from `../results/figures/` when compiling from `report/`. Add references only after the assets exist and are reviewed.
