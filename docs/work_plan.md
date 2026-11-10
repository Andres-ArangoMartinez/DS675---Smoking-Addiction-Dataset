# Work plan

## Current tasks

These immediate tasks are proposed; owners and dates await team agreement.

| Task | Owner | Status | Next action |
| --- | --- | --- | --- |
| Agree on the prediction scenario | Unassigned | Proposed | Discuss whom to predict for, how far ahead, and what information is available; update the [protocol overview](methodology.md#protocol-overview). |
| Select the dataset version | Unassigned | Proposed | Agree on a version and record its details in [data/README.md](../data/README.md). |
| Review the Kaggle references | Unassigned | Proposed | Review the two notebooks identified in Milestone 2 and document the [comparison basis](methodology.md#comparison-with-kaggle-work). |
| Define a small baseline task | Unassigned | Proposed | After the scenario and source review, agree on the task, owner, reviewer, and completion criterion. |

## Proposed stages

| Stage | Expected output | Depends on | Complete when |
| --- | --- | --- | --- |
| 1. Agree on question and scenario | Target, population, horizon, and information cutoff | Team discussion of Milestone 2 | The protocol overview specifies what a prediction means and may use |
| 2. Audit data and Kaggle references | Version/quality record, eligible features, and comparison basis | Scenario from stage 1 | Data characteristics and quality findings are recorded; reference versions, attribution, and intended extension are clear |
| 3. Build the baseline workflow | Shared preparation/evaluation code and a recorded baseline | Stages 1-2; agreed split and metrics | A teammate reruns the documented baseline; test data has not guided selection |
| 4. Compare models and feature groups | Experiment records and generated comparisons | Baseline; agreed candidates and tuning budget | Comparisons use identical eligible observations and evaluation rules, with deviations explained |
| 5. Interpret and write | Evidence-backed LaTeX report | Recorded comparisons; background writing can start earlier | Cross-review checks findings, limitations, attribution, contributions, links, and the 5-8 page length |
| 6. Reproduce and present | Reproduction check, agreed report PDF, and group video | Reviewed code and report | A teammate verifies the documented run; all members participate in a 5-10 minute video; final report and README links work |

The report must link to Milestone 2, code, and the final video. Record actual member work in [contributions.md](contributions.md). Log consequential choices or revisions in [decisions.md](decisions.md); keep the current protocol itself in [methodology.md](methodology.md).

## Rubric to evidence

Based on the supplied Milestone 4 rubric (15 points). These are planned evidence locations, not claims of completion.

| Criterion | Evidence the completed project must provide | Main locations |
| --- | --- | --- |
| Objectives (3) | Precise supervised task; dataset source, uses, record/feature characteristics, and suitability | Report introduction/data; data version record |
| Methodology (5) | Justified preparation, models, training/testing, validation/tuning, and fair Kaggle comparison | Report methodology/results; shared code; experiment records |
| Contributions and Originality (4) | Demonstrable extension beyond relevant Kaggle work; full external/internal attribution; equitable, significant coding/writing/presentation work by each member | Report introduction/discussion/contributions; contribution evidence; reference and code links |
| Presentation (3) | Clear, concise 5-8 page report with names, contributions, and required links; 5-10 minute group video that complements it with discussion, a demo, or further insight | LaTeX report and final PDF; presentation materials and final video |
