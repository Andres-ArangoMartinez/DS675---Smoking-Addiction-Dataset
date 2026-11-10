# Scientific protocol

## Protocol overview

Kate's Milestone 2 proposal is the starting point for team review. Distinguish **previously proposed by Kate**, **confirmed by the group** only when documented in [decisions.md](decisions.md), and **implemented or measured** only when supported by code and experiment evidence. No group confirmation or run evidence is recorded yet.

### Previously proposed by Kate

Source: [Milestone 2, pp. 13-14](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf#page=13).

| Part of the plan | Existing proposal | Source page |
| --- | --- | --- |
| Task and feature comparisons | Predict `Overall_Craving_Score`; compare psychological, lifestyle, and historical feature groups individually and in combination | 13-14 |
| Models | Ridge Regression, Random Forest, and XGBoost | 14 |
| Metrics | MAE, RMSE, and R-squared | 14 |
| Split | Training days 1-20, validation days 21-25, test days 26-30 | 14 |
| Preparation | Exploratory distributions, correlations, and trends; missing-value handling, scaling, and feature engineering following the reviewed historical-feature example | 14; historical example on [p. 7](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf#page=7) |

Review and refine this plan rather than selecting every element afresh. The prediction cutoff/horizon, evaluation population, exact feature columns, historical windows, and tuning procedure still need clarification and group agreement.

| Question | Basis for team review |
| --- | --- |
| What are we predicting? | `Overall_Craving_Score`, a numerical target for supervised regression |
| For whom and how far ahead? | Kate describes future observations but does not fix the horizon or consistently define the population. Next-day prediction for known participants is a possible clarification, not an agreed scenario or established original contribution. |
| What information is available? | Measurements available by a defined prediction cutoff, the time when a prediction would be made; exact columns and history remain to be chosen. |
| How will we train and evaluate? | Fit models on training data, select settings with scenario-appropriate validation, and evaluate once the protocol is fixed on a held-out test set. |
| What will demonstrate our contribution? | Implement and evaluate Kate's proposed feature-group comparison under consistent conditions; establish the extension beyond Kaggle work through verified source review and measured evidence. |

## Data and preparation

Keep source, version, hashes, characteristics, and acquisition details in [data/README.md](../data/README.md). Audit types, score ranges, missing values, duplicate participant-day keys, time order/gaps, and consistency of repeated participant attributes. Record findings and exclusion counts. Verify the target's scale and construction from source documentation.

Justify missing-value handling, categorical encoding, scaling, and any feature selection after the audit. Fit all learned preparation steps only on the training portion of each validation fold (a repeated train/validation partition), then apply them to validation/test data. Preserve raw files; shared code must recreate processed data.

## Features and availability

Kate's proposed groups cover psychological measurements (anxiety, stress, mood), lifestyle/daily habits (sleep, exercise, caffeine), and historical craving/nicotine use, individually and in combination. Confirm the group definitions and decide separately whether demographics or day information add useful context. Record exact columns, group combinations, and timing here or in a linked versioned configuration before comparisons.

**Leakage** means using information that reveals the target or would be unavailable when predicting. Exclude the target being predicted from the inputs. Correlation or same-day measurement alone does not establish leakage. Check both target construction and availability: a component used to calculate the target may make a comparison circular, while a same-day measurement can be valid for an estimation task if available at its cutoff. Forecasting has a different information boundary. Historical target values may be eligible when already observed.

Use participant IDs as grouping keys unless a predictive use is explicitly justified. Build lags (earlier measurements) and rolling summaries within each participant in time order, using only available history. Check gaps: the previous row may not be the previous day. Define how to handle insufficient history and use the same eligible evaluation observations across feature groups.

## Splits, training, and tuning

A split separates observations for fitting, choosing settings, and final evaluation. Match it to the scenario:

- **Known participants, future days:** consider chronological holdout and time-respecting validation. Specify whether earlier observed validation/test-day measurements become available for later one-step predictions. Predicting several days from one fixed starting point uses different history rules.
- **New participants:** separate participant groups across training, validation, and test; add time restrictions if forecasting is also required.

**Split tension to resolve:** [page 3](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf#page=3) says to keep each participant's observations in one train/test partition, while [page 14](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf#page=14) proposes splitting their days across training, validation, and test. These imply different evaluation populations. Resolve this only after agreeing on the prediction scenario; neither rule is confirmed here.

Random row splitting can mix related observations and does not demonstrate performance on unseen participants or future days. Confirm or revise Kate's proposed day boundaries, then record fold rules, counts, overlap checks, and history handling before fitting.

Review Kate's proposed models: Ridge Regression (regularized linear regression), Random Forest, and XGBoost (tree-based methods). Confirm or refine this small set, explaining each model's role and preparation needs. Consider a constant baseline (a simple training-only prediction) and persistence (the last observed target) if eligible; these baseline choices also need agreement.

Hyperparameter tuning chooses model settings using validation data. Define search spaces, budgets, stopping/selection rules, and random seeds in shared configuration or linked records. Use comparable tuning opportunities. Keep the final test set outside preprocessing fitting, feature selection, and tuning; fix the protocol before final evaluation. Record exceptions in the affected experiment.

## Metrics and comparison

Kate proposed mean absolute error (MAE), root mean squared error (RMSE), and R-squared. MAE is in target-score units; RMSE emphasizes larger errors; R-squared measures improvement relative to predicting the evaluation mean and can be negative. Confirm these metrics and select a primary metric before comparisons. Percentage errors may be unsuitable near zero.

Use identical eligible evaluation observations, split rules, and metric definitions for all feature/model comparisons. Decide row versus participant weighting and how to summarize uncertainty; repeated rows from a participant are not independent. Report gains over the baseline as well as differences between models.

## Comparison with Kaggle work

Kate reviewed *Time-Series Forecasting: Nicotine Craving and Anxiety Dynamics* and *Smoking Addiction Insights* in [Milestone 2, pp. 4-13](../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf#page=4). The numerical results summarized there are external reported findings, not experiments performed or reproduced by Kate or the group. Verify the original notebooks' exact URLs/versions, authors, target/horizon/population, features/preparation, split, tuning, and metrics. Document any actual method/code reuse, license conditions, and adaptations; cite verified sources in the report and code.

The feature-group comparison is Kate's proposed extension, not a newly introduced direction. Establish what it adds beyond those notebooks before claiming originality. Scores from different targets, populations, or splits provide context, not a fair ranking. State comparability limits or justify a matched reimplementation if undertaken.

## Limitations and run evidence

Synthetic data represents simulated relationships. Discuss generator artifacts, short time coverage, and limits on generalization to real nicotine-use behavior. Predictive association and feature importance do not establish causation or clinical usefulness.

Use the [experiment record](experiment_template.md) to link the exact protocol, data, code, environment, and settings used by each run. Shared dependency and execution information belongs in [src/README.md](../src/README.md). Confirm or refine the existing proposal and resolve its open details before implementing comparisons; measured findings require actual run evidence.
