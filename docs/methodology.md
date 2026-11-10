# Methodology planning template

**Status: editable proposal; scientific choices remain pending team agreement.** The project must use supervised prediction. The current direction is regression on `Overall_Craving_Score`, comparing information from different feature groups. Nothing below establishes a final split, model, feature set, or metric.

## 1. Research question and target

- Proposed question: how do psychological measurements, daily habits, and historical craving and nicotine-use information contribute to predicting `Overall_Craving_Score`?
- Agreed question and target definition: **pending**.
- Unit of prediction and intended interpretation: **pending**.
- Evidence for target definition, scale, and any construction from other columns: **pending dataset audit**. Exclude the target and any direct proxies or components that would reveal it at prediction time.

## 2. Prediction horizon and evaluation population

- Candidate: predict a known participant's next-day score using only information available by the agreed cutoff on the previous day.
- Alternative to discuss: prediction for participants not seen during fitting. Specify whether any history for these participants would be available.
- Agreed horizon, prediction cutoff, population, and required history: **pending**.
- Distinguish same-day estimation from forecasting. A column recorded after the prediction cutoff is unavailable even if it appears in the dataset.

## 3. Dataset source and version

Source: [Kaggle dataset](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data). The [Milestone 2 proposal](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf) describes it as synthetic longitudinal data; verify the actual downloaded schema and metadata before analysis.

Record the selected Kaggle version/date, original filenames, SHA-256 hashes, schema, row/participant counts, license, and acquisition steps in [data/README.md](../data/README.md). Do not assume a new download is the same version. Dataset selection and audit findings: **pending**.

## 4. Quality checks and preparation

Plan checks for types, score ranges, missingness, duplicate participant-day keys, ordering, gaps, and consistency of repeated participant attributes. Record exclusions and their counts. Confirm column meanings rather than inferring them from names alone.

Propose imputation, encoding, and scaling only after the audit. Fit learned preprocessing on each training fold, then apply it to validation/test data. Never fit preprocessing or feature selection on all observations before splitting. Retain the original raw files unchanged and document how shared code recreates processed data. Rules and implementation: **pending**.

## 5. Feature groups and information availability

| Candidate group | Examples to verify against the data | Decision needed |
| --- | --- | --- |
| Psychological measurements | Anxiety, stress, mood measurements | Which measurements exist before the prediction cutoff? |
| Daily habits | Sleep, exercise, caffeine measurements | Which day and recording time can be used? |
| Historical craving and nicotine use | Earlier craving scores and earlier nicotine-use measurements | Which lags/windows are justified, and how much history is required? |
| Context, if justified | Demographics and day information | Include, exclude, or use only for descriptive analysis? |

Exact column lists and group combinations: **pending**. Participant IDs are keys for grouping and ordering; do not automatically treat them as predictive features. Construct lags within each participant, ordered by time. Rolling features must use only observations available before the target cutoff. Check whether missing days mean a previous row is not the previous day. Define cold-start handling and a common eligible evaluation cohort before comparing groups.

## 6. Participant and temporal splits

The split must answer the agreed question. Random row splits can mix related participant observations and do not establish performance on new participants or future days.

- **Known participants, future days:** consider chronological holdout and time-respecting validation. Preserve prediction-time ordering within each participant and across evaluation boundaries. Specify whether observed earlier validation/test-day measurements may be used as history in a rolling one-step scenario; never use future values. A fixed-origin multi-step forecast has different information rules.
- **New participants:** consider disjoint participant groups for train, validation, and test. If forecasting is also required, combine participant separation with the appropriate temporal restrictions.
- Milestone 2 suggested days 1-20 / 21-25 / 26-30. That is an earlier proposal to review, not an agreed group protocol or evidence that the downloaded data supports it.

Agreed split rules, cutoff values, fold construction, overlap checks, and handling of incomplete histories: **pending**. Keep the final test set separate from feature/model selection.

## 7. Baselines and candidate models

Candidates for discussion: a training-only constant predictor; persistence from a previous observed score if available in the agreed scenario; Ridge regression; Random Forest; and XGBoost if justified and needed. No dependencies or models are installed by this setup.

Agree on a small, justified comparison before implementation. State each model's purpose, preprocessing needs, and tuning budget. Distinguish improvements over a simple baseline from differences between complex models. Final candidates: **pending**.

## 8. Validation and tuning

Select time-aware and/or participant-aware folds to match Section 6. Define validation metric, hyperparameter search space, search budget, stopping rules, seeds, and preprocessing pipeline before tuning. Use the same evaluation observations and comparable tuning opportunities across models and feature groups. Document all deviations. Lock the protocol before final test evaluation; do not repeatedly select models using test scores. Protocol: **pending**.

## 9. Evaluation metrics and comparisons

Candidate primary metric: MAE, because it is expressed in target-score units. Supporting candidates: RMSE and R-squared. These choices are **not agreed**. Explain any selected metric's meaning and limitations; for example, R-squared may be negative, and percentage errors can be unsuitable near zero.

Decide how repeated observations are weighted (by row or by participant), how uncertainty will be summarized, and whether paired per-participant comparisons are useful. Do not assume rows are independent when computing uncertainty. Compare feature groups on the same eligible evaluation observations so differences are not caused by a changed cohort. Metrics and comparison protocol: **pending**.

## 10. Relevant Kaggle work and attribution

Milestone 2 discusses *Time-Series Forecasting: Nicotine Craving and Anxiety Dynamics* and *Smoking Addiction Insights*. Treat those descriptions as leads; inspect the original notebooks before relying on their methods or numerical claims. Exact URLs, versions, authorship, and reuse permissions still need verification.

| Reference and exact version link | Target / horizon / population | Features and preparation | Split, tuning, metrics | Reused method or code and attribution | Our verified difference |
| --- | --- | --- | --- | --- | --- |
| Pending source review | Pending | Pending | Pending | Pending | Pending |

Proposed differentiation: a coordinated comparison of psychological, habit, and historical feature groups under one explicitly defined information boundary and evaluation scenario. Verify that this adds something beyond the relevant notebooks; do not claim novelty before the review. Published scores with different targets, cohorts, or splits are context, not a fair direct ranking. Record a matched reimplementation only if actually performed and attributed.

## 11. Synthetic-data limitations

Discuss simulated relationships, possible generator artifacts, limited time coverage, and the gap between predictive performance on synthetic observations and real nicotine-use behavior. Do not make clinical claims or infer causation from feature importance or predictive associations. Record additional limitations discovered during the audit.

## 12. Questions requiring agreement

- What exactly is predicted, for whom, and how far ahead?
- What is available at the prediction cutoff, including historical target measurements?
- Which dataset version, feature groups, history windows, and eligible observations will be used?
- Which split, validation folds, baselines, models, tuning budget, seeds, and metrics are justified?
- What is the verified difference from Kaggle work, and what needs attribution?
- How will members share coding, writing, review, and presentation work?

Move actual agreements into [decisions.md](decisions.md), link evidence, and update this template. Use [experiment_template.md](experiment_template.md) for actual runs; this document alone does not make the project reproducible.
