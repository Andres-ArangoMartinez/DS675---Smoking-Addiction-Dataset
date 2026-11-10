# Scientific protocol

## Protocol overview

**Status: proposed.** The team has not approved a prediction scenario or experimental protocol. Update this page as choices are agreed; use [decisions.md](decisions.md) for the reasons behind consequential choices.

| Question | Current proposal |
| --- | --- |
| What are we predicting? | `Overall_Craving_Score`, a numerical target for supervised regression |
| For whom and how far ahead? | Candidate: the next day for known participants. Prediction for new participants is an alternative to discuss. |
| What information is available? | Measurements available by a defined prediction cutoff, the time when a prediction would be made; exact columns and history remain to be chosen. |
| How will we train and evaluate? | Fit models on training data, select settings with scenario-appropriate validation, and evaluate once the protocol is fixed on a held-out test set. |
| What will demonstrate our contribution? | Compare psychological, habit, and historical feature groups under the same evaluation conditions; establish the extension beyond Kaggle work through source review and measured evidence. |

## Data and preparation

Keep source, version, hashes, characteristics, and acquisition details in [data/README.md](../data/README.md). Audit types, score ranges, missing values, duplicate participant-day keys, time order/gaps, and consistency of repeated participant attributes. Record findings and exclusion counts. Verify the target's scale and construction from source documentation.

Justify missing-value handling, categorical encoding, scaling, and any feature selection after the audit. Fit all learned preparation steps only on the training portion of each validation fold (a repeated train/validation partition), then apply them to validation/test data. Preserve raw files; shared code must recreate processed data.

## Features and availability

Candidate groups are psychological measurements (anxiety, stress, mood), daily habits (sleep, exercise, caffeine), and historical craving/nicotine use. Decide separately whether demographics or day information add useful context. Record exact columns, group combinations, and timing here or in a linked versioned configuration before comparisons.

**Leakage** means using information that reveals the target or would be unavailable when predicting. Exclude the target being predicted from the inputs. Correlation or same-day measurement alone does not establish leakage. Check both target construction and availability: a component used to calculate the target may make a comparison circular, while a same-day measurement can be valid for an estimation task if available at its cutoff. Forecasting has a different information boundary. Historical target values may be eligible when already observed.

Use participant IDs as grouping keys unless a predictive use is explicitly justified. Build lags (earlier measurements) and rolling summaries within each participant in time order, using only available history. Check gaps: the previous row may not be the previous day. Define how to handle insufficient history and use the same eligible evaluation observations across feature groups.

## Splits, training, and tuning

A split separates observations for fitting, choosing settings, and final evaluation. Match it to the scenario:

- **Known participants, future days:** consider chronological holdout and time-respecting validation. Specify whether earlier observed validation/test-day measurements become available for later one-step predictions. Predicting several days from one fixed starting point uses different history rules.
- **New participants:** separate participant groups across training, validation, and test; add time restrictions if forecasting is also required.

Random row splitting can mix related observations and does not demonstrate performance on unseen participants or future days. Milestone 2's days 1-20 / 21-25 / 26-30 split is an earlier suggestion, not an agreed protocol. Record chosen boundaries, fold rules, counts, overlap checks, and history handling before fitting.

Start with a constant baseline (a simple training-only prediction), and consider persistence (the last observed target) if eligible. Candidate models are Ridge regression (regularized linear regression), Random Forest, and XGBoost (tree-based methods). Select a small justified set, explaining each model's role and preparation needs.

Hyperparameter tuning chooses model settings using validation data. Define search spaces, budgets, stopping/selection rules, and random seeds in shared configuration or linked records. Use comparable tuning opportunities. Keep the final test set outside preprocessing fitting, feature selection, and tuning; fix the protocol before final evaluation. Record exceptions in the affected experiment.

## Metrics and comparison

Candidate primary metric: mean absolute error (MAE), in target-score units. Supporting candidates: root mean squared error (RMSE), which emphasizes larger errors, and R-squared, improvement relative to predicting the evaluation mean; it can be negative. Select and justify the metrics before comparisons. Percentage errors may be unsuitable near zero.

Use identical eligible evaluation observations, split rules, and metric definitions for all feature/model comparisons. Decide row versus participant weighting and how to summarize uncertainty; repeated rows from a participant are not independent. Report gains over the baseline as well as differences between models.

## Comparison with Kaggle work

Milestone 2 identifies *Time-Series Forecasting: Nicotine Craving and Anxiety Dynamics* and *Smoking Addiction Insights*. Review their original notebooks and record exact URLs/versions, authors, target/horizon/population, features/preparation, split, tuning, and metrics here. Explain which methods or code were reused, their license conditions, and adaptations; cite verified sources in the report and code.

The proposed extension is a coordinated feature-group comparison. Establish what it adds beyond those notebooks before claiming originality. Scores from different targets, populations, or splits provide context, not a fair ranking. State comparability limits or justify a matched reimplementation if undertaken.

## Limitations and run evidence

Synthetic data represents simulated relationships. Discuss generator artifacts, short time coverage, and limits on generalization to real nicotine-use behavior. Predictive association and feature importance do not establish causation or clinical usefulness.

Use the [experiment record](experiment_template.md) to link the exact protocol, data, code, environment, and settings used by each run. Shared dependency and execution information belongs in [src/README.md](../src/README.md). Scenario, data version, features, split, models, tuning, and metrics are the choices still to resolve before implementing comparisons.
