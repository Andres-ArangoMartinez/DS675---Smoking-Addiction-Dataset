# Proposed Supervised Learning Objective

## Learning objective

Evaluate how much psychological and lifestyle measurements contribute to **predicting next-day nicotine craving**, beyond a participant's previously observed craving and nicotine-use history. This refines the feature-group comparison proposed in [Kate Sazonova's Milestone 2](../../../Smoking%20Addiction%20Dataset%20Sazonova_Milestone%202.pdf) by specifying the prediction horizon and the information available when a prediction is made.

## Proposed prediction task

| Element | Definition |
| --- | --- |
| **Learning type** | Supervised **regression**. |
| **Target attribute** | `Overall_Craving_Score` for participant *i* on day *t + 1*. |
| **Prediction unit** | One future participant–day observation: (*Participant_ID*, *Day_Number = t + 1*). |
| **Prediction horizon and cutoff** | **One day ahead**, with the prediction issued at the **end of day *t***. |
| **Eligible input information** | Previously observed participant characteristics and craving/nicotine-use history through day *t*; psychological and lifestyle measurements recorded by the end of day *t*. |
| **Evaluation population** | Future days of **previously observed simulated participants**, not entirely unseen participants. |
| **Expected output** | A numerical craving score on the dataset's observed **0–10 scale**; no class label or classification threshold. |

Formally, the intended prediction is

$$
\widehat{y}_{i,t+1}=f\!\left(\text{profile}_i,\ \text{history}_{i,\leq t},\ \text{psychology}_{i,t},\ \text{lifestyle}_{i,t}\right),
\qquad y_{i,t+1}=\texttt{Overall\_Craving\_Score}_{i,t+1}.
$$

**Information boundary.** No measurements from day *t + 1* may enter the prediction for that day. `Participant_ID` identifies the sequence for assembling observations; it is not, by itself, a proposed predictive feature. Missing target values must not be treated as observed scores or assigned an invented label. Exact eligible features, missing-data rules, split dates, and model choices belong in the [scientific protocol](../../../docs/methodology.md), not in this objective statement.

## Scope and documentary basis

This task uses the dataset's daily participant-level structure to distinguish **forecasting a later craving score** from estimating craving with contemporaneous measurements. It is a prediction problem within **synthetic** records; it does not establish clinical validity, causality, or performance on real nicotine users. The [dataset description and audit](../02_dataset_description/dataset_description.md) document the data characteristics and limitations; the [related-work review](../01_related_work_sources/Background.md) discusses relevant empirical and methodological precedents. Data version and provenance are tracked in the [data record](../../../data/README.md).

## Comparison with Kate's Milestone 2 proposal

This proposal **retains Kate's target and feature-group comparison** while making the prediction scenario more explicit. The differences are limited to the following clarifications:

| Aspect | Kate's Milestone 2 proposal | Current proposal |
| --- | --- | --- |
| **Target and learning task** | Predict `Overall_Craving_Score` using supervised regression. | **Unchanged.** |
| **Prediction horizon** | Future observations; no fixed forecast horizon. | Predict the score **one day ahead** (*t + 1*). |
| **Information cutoff** | Timing of available predictors not explicitly specified. | Use only information available **by the end of day *t***. |
| **Evaluation population** | Participant-grouped and chronological splitting are both discussed, without a single defined population. | Forecast future days for **previously observed participants**. |
| **Feature-group comparison** | Compare psychological, lifestyle, and historical variables separately and in combination. | Retain these groups, emphasizing their **additional value beyond observed history**. |

These are proposed refinements, **not yet recorded as group-approved decisions**. See the [scientific protocol](../../../docs/methodology.md) and [decision log](../../../docs/decisions.md) for their formal status.
