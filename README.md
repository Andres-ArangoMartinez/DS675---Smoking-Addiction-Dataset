# DS675 Milestone 4: Smoking Addiction Dataset

We are preparing a supervised machine learning group project using the Smoking Addiction Dataset. This repository currently contains the original Milestone 2 proposal and a planning and report-writing structure. Data preparation, experiments, results, and scientific reproducibility have not yet been implemented or validated.

**Group members:** Kate Sazonova, Nahreg Rastguelenian, and Andres Arango Martinez.

## Proposed research direction: pending team agreement

Compare how psychological measurements, daily habits, and historical craving and nicotine-use information contribute to predicting `Overall_Craving_Score` through supervised regression. Next-day prediction for known participants is one candidate scenario. The prediction horizon, evaluation population, feature groups, and experimental protocol still need agreement. Models and splits suggested in Milestone 2 are starting points for discussion, not finalized group decisions.

- [Dataset on Kaggle](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data)
- [Original Milestone 2 proposal](Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf) (kept at its original location)
- [Project repository](https://github.com/Andres-ArangoMartinez/DS675---Smoking-Addiction-Dataset)

## Start here

1. Read the [proposed work plan](docs/work_plan.md) and discuss the open questions in the [methodology template](docs/methodology.md).
2. Record agreements in the [decision log](docs/decisions.md).
3. Follow the small-task workflow in [CONTRIBUTING.md](CONTRIBUTING.md).
4. Record completed work and evidence in the [member contribution record](docs/contributions.md).

## Where things belong

| Location | Purpose |
| --- | --- |
| [docs/](docs/) | Planning, decisions, contributions, and the experiment template |
| [data/](data/README.md) | Dataset acquisition instructions; local raw and processed data |
| [work/](work/README.md) | Individual exploration in `kate/`, `nahreg/`, or `andres/` |
| [src/](src/README.md) | Reviewed, reusable preparation, modeling, and evaluation code |
| [notebooks/](notebooks/README.md) | Integrated analyses that use shared code |
| [results/](results/README.md) | Recorded experiments, comparison tables, and figures |
| [report/](report/README.md) | Shared LaTeX source and report instructions |
| [presentation/](presentation/README.md) | Presentation outline and supporting materials |

## Report and deliverables

The official shared report source is LaTeX in [report/main.tex](report/main.tex), with separate [section files](report/sections/). Edit those files through reviewed changes; Google Docs is not the official report-writing location.

From `report/`, with a local LaTeX installation, run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See the [report guide](report/README.md) for preview, page-count, and final-PDF instructions.

| Deliverable | Current status |
| --- | --- |
| Results | Pending: no experiments have been run for this setup. See the [results guide](results/README.md). |
| Final group report (5-8 pages) | Pending: the drafting template is not the final report. The agreed PDF will be stored at `report/final_report.pdf`. |
| Final group video (5-10 minutes) | Pending: no video URL yet. Every member must participate. |

The final report must link to the original Milestone 2 proposal, code, and final video. All three members must contribute to coding, writing, and presentation. Clearly attribute external methods and code, and explain how the project differs from relevant Kaggle work.
