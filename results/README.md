# Recorded outputs

- `experiments/<experiment-id>/`: one output location per run, with a `record.md` based on the [experiment template](../docs/experiment_template.md). Link versioned shared settings and keep measured results and interpretation together.
- `tables/`: shared comparison tables, generated from experiment records when the workflow exists.
- `figures/`: selected figures with captions, regeneration commands, and links to the source experiments.

Track compact records, small metric CSVs, and reviewed tables/figures. Keep large predictions, models, caches, data copies, videos, and temporary outputs out of Git. Use local `scratch/` or `cache/` folders for temporary run outputs. Check file sizes and changed files; ignore rules cannot catch every large artifact. For any shared external artifact, record its location, hash, and retrieval or regeneration method.

See the [report guide](../report/README.md#using-results-and-submitting) for including existing assets in LaTeX.
