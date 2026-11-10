# Working together

**Agree on a task → work on it → share it → teammate review → integrate.**

1. **Agree on a small task.** Use team discussion, the [work plan](docs/work_plan.md), or an optional GitHub Issue (a task card). Agree who will do it, who can review it, and what would make it complete.
2. **Work on it.** For shared changes, use a short-lived branch: a separate workspace in Git for one task. In GitHub Desktop, start from current `main`, select **Current Branch > New Branch**, and use a name such as `analysis/baseline`. Save focused changes in commits with descriptive messages.
3. **Share an advance.** Explain what changed, what you checked, and what help you need. An unfinished exploration can be shared for feedback. For integration, publish the branch and open a pull request: a request to bring its changes into `main`.
4. **Review and integrate.** Another teammate reviews substantive shared changes, including code, analyses, protocol choices, and report content. Resolve comments, merge the ready work, and update local `main`. A small typo does not need a separate Issue or formal decision entry.

GitHub Desktop can handle these steps; detailed Git commands are not required to start contributing. Ask a teammate to help with an unfamiliar branch or pull request.

## Where to work

| Location | Use |
| --- | --- |
| [work/kate/](work/kate/), [work/nahreg/](work/nahreg/), [work/andres/](work/andres/) | Individual exploration; these folders do not assign responsibilities |
| [src/](src/README.md) | Reviewed reusable preparation, modeling, and evaluation code |
| [notebooks/](notebooks/README.md) | Integrated analyses using shared code |
| [results/](results/README.md) | Recorded experiments and shared comparison outputs |
| [report/](report/README.md) | Official report writing in separate LaTeX section files |

Coordinate one editor at a time for each notebook or report section. Use the common dataset under `data/` and shared preparation/evaluation code; avoid competing copies. Inspect changed files before sharing so credentials, large temporary outputs, and local data stay out of Git.

Keep the current scientific protocol in [methodology.md](docs/methodology.md). Use [decisions.md](docs/decisions.md) for consequential agreements or changes, and [contributions.md](docs/contributions.md) for meaningful completed work with evidence. These are not forms to fill for every small edit. Attribute external methods and adapted code where used, including source/version and license conditions.
