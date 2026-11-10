# Working together

Keep tasks small and ask a teammate to review before merging into `main`. Main contains reviewed, integrated project work. No remote Issues or pull requests are created by this repository setup.

## One task at a time

1. **Define a GitHub Issue.** An Issue is a shared task card. Describe the problem, expected output, and a completion criterion that another person can check. Agree on a responsible member and a different reviewer; do not assume assignments from folder names.
2. **Create a short-lived branch.** A branch keeps one task's changes separate until review. Use a short name such as `docs/research-question` or `analysis/baseline`. In GitHub Desktop, select this repository, use **Current Branch > New Branch**, and start from the team's current `main`.
3. **Make focused changes.** Work on the agreed task, inspect the changed files in GitHub Desktop, and keep unrelated edits separate. Save work in small commits with descriptive messages. Do not include credentials, local data, or large temporary outputs.
4. **Open a pull request when ready.** Publish your task branch from GitHub Desktop when the work is ready for team review, then create a pull request. A pull request proposes merging a branch into `main`. Link the Issue, explain what changed and why, list verification actually performed, and identify open limitations. Do not describe pending checks as passed.
5. **Get another teammate's review.** The reviewer checks the completion criterion, code or text, and relevant outputs. Resolve comments before merging. Update your local `main` after the merge and retire the completed branch.

These are instructions for future team work, not a request to create Issues, commits, or pull requests during setup.

## File conventions

- `work/<name>/` is for individual exploration: `kate/`, `nahreg/`, and `andres/`. Folder ownership does not assign project responsibilities.
- Reviewed reusable code belongs in `src/`. Share preparation and evaluation functions instead of making competing copies.
- Integrated analyses belong in `notebooks/`. Avoid editing the same notebook simultaneously; agree on one editor and a reviewer for each task.
- Recorded experiment outputs belong in `results/experiments/<experiment-id>/`. Use the [experiment template](docs/experiment_template.md).
- Shared comparison tables and figures belong in `results/tables/` and `results/figures/` and should be generated from recorded experiments once that workflow exists.
- Report writing happens in `report/sections/`. Coordinate section ownership for each task and have someone else cross-review it. Use `main.tex` for shared formatting.
- Keep one local raw dataset in `data/raw/`; do not copy datasets into individual work folders. See [data instructions](data/README.md).

## Before requesting review

- Explain how you checked your change. For future code, include the command, data version, and relevant output; for report edits, compile and visually review the complete PDF.
- Record agreed choices in [decisions](docs/decisions.md) and actual completed work in [contributions](docs/contributions.md).
- Add source links and attribution for borrowed ideas or code, including what was adapted. Check source licenses before reuse. Never present another notebook's results as this team's results.
- Keep proposed methods and expected outcomes labeled as proposals until agreed or measured. Do not commit large logs, videos, models, or temporary data just to share them; agree on a storage location and link it instead.
