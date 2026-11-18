# DS675 — Dataset Description and Validation

*Supporting document for the Milestone 4 “Dataset Description and Learning Objective” section.*

## 1. Dataset description

**Scope.** Describe and assess the dataset.

**Evidence.** The counts and statistics below come from inspecting all **30,000 records in a public CSV copy** in [NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction/blob/main/Dataset/Nicotine_Craving_Anxiety_Dynamics_30Days.csv). The initial audit covered the full file on GitHub. The common [local CSV](../../../data/raw/Nicotine_Craving_Anxiety_Dynamics_30Days.csv) has the same byte size, SHA-256, and Git blob identifier. The [statistical audit](dataset_audit_AI_assisted/README.md) reproduces the numerical findings; the complementary [provenance verifier](../../../data/provenance_AI_assisted/README.md) checks source metadata and file identity. Their scope and evidence are summarized in section 1.9 and [data/README.md](../../../data/README.md). The [Kaggle dataset page](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data) remains the publication reference.

### Review framework

The review used five analytical perspectives to **describe the available resource accurately**.

| Perspective | Guiding question | Evidence examined |
| --- | --- | --- |
| **Data auditing / engineering** | Is the CSV readable, intact, and consistent in its keys and types? | Rows, columns, duplicates, ranges, formats, and missing values |
| **Descriptive statistics** | How are the records and measurements distributed? | Frequencies, quartiles, dispersion, and craving distribution |
| **Longitudinal analysis** | What do repeated measurements represent, and how do they vary within participants? | Participant–day panel, profile stability, within-person variation, and descriptive temporal correlation |
| **Scientific and synthetic-data validity** | Which interpretations are warranted, and which require the generator's definitions? | Field semantics, lack of a clinical instrument, and limits to generalization |
| **Academic rubric review** | Does the description provide enough information to assess the resource? | Source, potential uses, information types, dimensions, data types, integrity, limitations, and traceability |

### 1.1 Identification, provenance, and nature

- **Kaggle name:** *Smoking Addiction Dataset / The Nicotine Craving and Anxiety Dynamics Dataset*.
- **Publisher identified by the official URL:** `datascikhan` (DataSciKhan). [Kaggle listing](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data).
- **Inspected format:** a tabular CSV with a header, named `Nicotine_Craving_Anxiety_Dynamics_30Days.csv`.
- **Nature:** **synthetic data** simulating oral nicotine pouch use, craving intensity (desire to use), psychological states, and daily habits. These are not clinical records from 1,000 real people.
- **Observation unit:** one **simulated participant on one day**, identified by `Participant_ID`–`Day_Number`.
- **Potential academic uses:** exploring repeated measurements; describing associations among craving, anxiety, consumption, and habits; and illustrating supervised regression or classification after explicitly choosing an outcome. **The dataset has no single predefined class label**: it contains both numeric scores and categorical indicators.

Although the fields refer to constructs used in nicotine research, a simulation cannot be assumed to reproduce real human magnitudes, associations, or responses faithfully. The 30 days are **consecutive indices within each participant**. The CSV provides neither a calendar start date nor complete assessment timestamps. `First_Pouch_Time` is a time of day (HH:MM), not a timestamp that independently identifies the observation date.

### 1.2 Size and longitudinal structure

| Characteristic | CSV result |
| --- | ---: |
| Data rows | **30,000** |
| Columns | **35** |
| Distinct participants | **1,000** |
| Distinct `Day_Number` values | **30 (1–30)** |
| Observations per participant | **30 for every participant** |
| Observations per day index | **1,000 for every day** |
| Duplicate participant–day keys | **0** |
| Duplicate full rows | **0** |
| Rows with an incorrect field count | **0** |
| Participants with inconsistent profiles across days | **0** (across the four fields checked) |

The **keys form a balanced panel**: all participants have all 30 days. This does **not** mean every cell is observed. Rows from the same participant are related and must not be described as 30,000 independent subjects. `Age_Group`, `Gender`, `Occupation_Status`, and `Nicotine_Use_Duration_Months` remain constant within each participant across the 30 days.

### 1.3 Inventory and conceptual grouping of the 35 columns

These **analytical groupings** align with the course review; they are not a formal ontology or a data dictionary published by the generator.

| Thematic group | Columns | Content |
| --- | ---: | --- |
| Participant and temporal identification | **2** | Participant key and day index |
| Demographics | **3** | Age group, gender, and occupation |
| Nicotine use and craving | **15** | Use duration, pouches, dose, use timing, scores, and resistance |
| Psychological states | **7** | Anxiety, stress, mood, irritability, and restlessness |
| Habits and activities | **8** | Sleep, caffeine, exercise, screen time, work/study, stressful events, and social interaction |
| **Total** | **35** | |

**Observed data types:** **20 `float64`**, **6 `int64`**, and **9 `object`** columns. Categories and `Yes`/`No` indicators are stored as text; `First_Pouch_Time` is a time string. Conceptually integer quantities such as `Exercise_Minutes` and `Time_Since_Last_Pouch_Minutes` may be inferred as `float64` when loaded with `NaN`.

### 1.4 Simulated participant profiles

Frequencies count **each `Participant_ID` once** (base = 1,000), rather than its 30 repeated rows.

| Variable | Categories and participant counts |
| --- | --- |
| `Age_Group` | 18–24: **239**; 25–34: **353**; 35–44: **203**; 45–54: **122**; 55+: **83** |
| `Gender` | Female: **482**; Male: **453**; Non-binary: **41**; Prefer_not_to_say: **24** |
| `Occupation_Status` | Employed: **488**; Student: **156**; Self_Employed: **123**; Unemployed: **88**; Retired: **82**; Homemaker: **63** |

The file records age groups, not exact ages. Gender categories retain the file's labels without further interpretation. These distributions describe **the simulated population in this copy**, not the demographics of real nicotine use.

### 1.5 Descriptive measurement statistics

Ranges are **observed minima and maxima**. The examples cover intensity, quantity, and duration.

| Field | Observed N | Minimum–maximum | Mean | Median |
| --- | ---: | ---: | ---: | ---: |
| `Pouches_Per_Day` | 30,000 | 0–24 | 7.431 | 7 |
| `Pouch_Strength_mg` | 30,000 | 4–15 | 7.859 | 8 |
| `Overall_Craving_Score` | 29,651 | 0–10 | 5.995 | 6.0 |
| `Daily_Anxiety_Score` | 30,000 | 0–10 | 5.312 | 5.3 |
| `Perceived_Stress_Score` | 30,000 | 0–10 | 3.119 | 2.7 |
| `Sleep_Duration_Hours` | 30,000 | 3.5–11 | 7.003 | 7.0 |
| `Sleep_Quality_Score` | 30,000 | 3–10 | 6.920 | 6.9 |
| `Caffeine_Intake_mg` | 30,000 | 0–600 | 160.495 | 140 |
| `Exercise_Minutes` | 29,630 | 0–180 | 30.047 | 25 |
| `Screen_Time_Hours` | 29,627 | 1–14 | 4.025 | 3.4 |
| `Social_Interaction_Hours` | 29,647 | 0–10 | 2.250 | 1.8 |

`Craving_Triggers` has **12 observed categories**; the most frequent are `Stress` (**6,077 records**) and `Boredom` (**3,505**), counted among nonempty cells. `Major_Stress_Event_Today` contains **1,476** `Yes` and **28,524** `No` records. These counts describe the coding; they do not establish that triggers or events cause craving.

### 1.6 Overall craving score and distribution

`Overall_Craving_Score` is a numeric score and **one possible outcome**. It is described here **without defining a prediction task**. Its formula, psychometric validation, and simulation origin could not be established from the CSV alone.

| Indicator | Calculated value |
| --- | ---: |
| Total records | 30,000 |
| Observed values | **29,651 (98.84%)** |
| Missing values | **349 (1.16%)** |
| Minimum / maximum | **0 / 10** |
| Mean | **5.994904** |
| Median | **6.0** |
| Sample standard deviation | **1.684405** |
| Lower quartile (Q1) / upper quartile (Q3) | **4.8 / 7.2** |
| Within-participant variation across days | **1,000 of 1,000** participants have more than one distinct observed value |
| Observed measurements per participant | **27–30** |

**Frequency distribution.** Each interval excludes its upper endpoint, except the final interval, which includes 10.

| Interval | Records | Interval | Records |
| --- | ---: | --- | ---: |
| [0, 1) | 28 | [5, 6) | 6,659 |
| [1, 2) | 163 | [6, 7) | 6,404 |
| [2, 3) | 833 | [7, 8) | 4,614 |
| [3, 4) | 2,405 | [8, 9) | 2,704 |
| [4, 5) | 4,601 | [9, 10] | 1,240 |

Scores concentrate in the middle: the central 50% lies between **4.8 and 7.2**. Observed daily means range from approximately **5.957 to 6.044**. Stable aggregate means do not establish temporal independence or rule out individual patterns. Morning, afternoon, and evening scores are columns in a daily record; they must **not** be described as a high-frequency EMA sequence without a documented schedule of independent measurements.

### 1.6.1 Temporal structure: within- and between-participant variation

The **30 observations per participant** distinguish two sources of variation. All 1,000 participants have at least two distinct observed `Overall_Craving_Score` values, while their **individual means** range from approximately **1.49 to 9.84**. This between-participant heterogeneity matters when interpreting pooled statistics.

Across **28,338 consecutive-day pairs** with both scores observed, Pearson correlation pooled across participants and days is approximately **0.859**. After subtracting each participant's observed mean from their scores, the correlation between consecutive-day deviations is approximately **−0.035**. This comparison is **not a predictive evaluation**: the pooled coefficient largely reflects stable differences between participants and must not be equated with autocorrelation of within-person fluctuations. The centered coefficient is descriptive and depends partly on the centering method; it does not by itself establish statistical independence or a lack of temporal information.

Day indices **1–30** provide neither calendar dates nor complete daily assessment timestamps. They do not establish hourly EMA or 30 days on a shared population calendar.

### 1.7 Integrity, missingness, and consistency

The longitudinal keys are complete, but **14 of 35 columns** contain missing values:

- **4,982 empty cells** out of 1,050,000 (**approximately 0.47%**).
- **4,630 rows** with at least one missing value (**15.43%** of 30,000).
- **21 complete columns** and **14 incomplete columns**.
- Missingness of **1.08%–1.27%** in incomplete columns.
- **349 missing `Overall_Craving_Score` values**, which are neither absent records nor values to replace automatically with zero.

| Incomplete column | Missing | % of 30,000 |
| --- | ---: | ---: |
| `Longest_Nicotine_Free_Period_Hours` | 380 | 1.27% |
| `Afternoon_Cravings_Score` | 373 | 1.24% |
| `Screen_Time_Hours` | 373 | 1.24% |
| `Exercise_Minutes` | 370 | 1.23% |
| `Morning_Cravings_Score` | 369 | 1.23% |
| `Successfully_Resisted` | 357 | 1.19% |
| `Time_Since_Last_Pouch_Minutes` | 355 | 1.18% |
| `Social_Interaction_Hours` | 353 | 1.18% |
| `Overall_Craving_Score` | 349 | 1.16% |
| `Evening_Anxiety_Score` | 347 | 1.16% |
| `Evening_Cravings_Score` | 346 | 1.15% |
| `Attempted_To_Resist_Craving` | 345 | 1.15% |
| `Mood_Score` | 342 | 1.14% |
| `Craving_Triggers` | 323 | 1.08% |
| **Total** | **4,982** | **0.47% of all cells** |

Syntax and range checks detected none of the following: scores outside [0,10] in the 13 score fields checked; negative values in 13 selected quantity and duration fields; invalid `HH:MM` values in `First_Pouch_Time`; categories other than `Yes` or `No` in the three binary indicators; or within-participant changes in the four stable profile fields.

These checks establish **basic internal consistency**, not physiological plausibility, random missingness, measurement independence, or realistic human behavior in the simulator. No audited formula explains how `Overall_Craving_Score` was derived from other fields.

### 1.7.1 Semantic checks requiring field definitions

Cross-field checks identified observations that **must not be classified automatically as errors** without the data dictionary or generation procedure.

| Cross-field check | Observed result | Interpretation |
| --- | ---: | --- |
| `Pouches_Per_Day = 0` with a `First_Pouch_Time` value | **358 records** | Unexpected if the time necessarily denotes the first pouch consumed *that day*, but it could be a habitual or scheduled time. A definition is needed. |
| `Pouches_Per_Day = 0` with `Time_Since_Last_Pouch_Minutes` observed | **355 records** | Not necessarily inconsistent if the last pouch preceded the recorded day; the interval's meaning is unknown. |
| `Overall_Craving_Score` exceeds `Craving_Intensity_Peak` | **7,078 records** with an observed outcome | Unexpected under literal “daily peak” and “daily average” definitions, but field names do not establish comparable score components. |
| `Successfully_Resisted = Yes` and `Attempted_To_Resist_Craving = No` | **0 records** | This apparent incompatibility was not observed in the reported fields. |
| `Overall_Craving_Score` missing with all three morning/afternoon/evening scores observed | **339 records** | Observed components do not justify reconstructing the overall score without its verified formula. |

These are **field-definition and semantic-quality flags**, not evidence of faulty generation or clinical invalidity. The CSV supports checks of values and proposed logical relationships, not the author's intent. Neither a validated clinical scale nor an overall score equal to the arithmetic mean of morning, afternoon, and evening scores should be assumed.

### 1.8 Suitability and limitations for supervised learning coursework

The dataset is **structurally suitable** for supervised learning coursework: it offers a potential numeric outcome, numeric and categorical predictors, 1,000 ordered individual series, and a manageable file size. Binary indicators could serve as outcomes for other tasks; **the file has no single predefined class assignment**.

Its suitability has six qualifications:

1. **Simulation, not a clinical cohort:** the apparent sample does not represent 1,000 real people or support medical extrapolation.
2. **Short horizon without calendar dates:** 30 day positions do not document calendar trends, annual seasonality, or time zones.
3. **Incomplete measurements:** 349 overall craving scores are missing, as are values in 13 additional columns.
4. **Incomplete field definitions:** without the generator or a formal dictionary, flags involving `Pouches_Per_Day`, `First_Pouch_Time`, `Overall_Craving_Score`, and `Craving_Intensity_Peak` remain unresolved, and mechanical relationships among same-day scores cannot be ruled out.
5. **Dependence and heterogeneity:** a participant's 30 records are not statistically independent observations; pooled correlation differs from within-participant correlation.
6. **Provenance and versioning:** the common CSV matches Kaggle version 1 and the GitHub copy pinned in the source record; section 1.9 links the reproducible checks and recorded comparison. Version, file identity, and the publisher-reported license are documented. These checks do not validate the simulation or its score construction.

The resource should therefore be presented as **synthetic longitudinal data for examining ML techniques and relationships within the simulation**, not evidence of prevalence, clinical efficacy, or causality.

### 1.9 Provenance and verification record

| Item | Status and evidence |
| --- | --- |
| Publication page | [Kaggle — DataSciKhan](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data) |
| CSV copy inspected and audited | [GitHub — NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction/blob/main/Dataset/Nicotine_Craving_Anxiety_Dynamics_30Days.csv) |
| File | `Nicotine_Craving_Anxiety_Dynamics_30Days.csv` |
| Inspected file size | **4,286,125 bytes** |
| Inspected file SHA-256 | `7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907` |
| Git blob identifier | `80bbba4a3289940698a2926618bf0f5f1525e69f` |
| Content audit | **Complete for this copy:** structure, inferred types, missingness, ranges, duplicates, profiles, statistics, and preliminary semantic checks. The [AI-assisted reproduction](dataset_audit_AI_assisted/README.md) matches **299/299 numerical and structural assertions** at the published precision |
| Exact Kaggle file version and license | The bundled [publisher metadata snapshot](../../../data/provenance_AI_assisted/evidence/kaggle_metadata_20261116.json), recorded on 2026-11-16, identifies dataset `11749711`, version 1, and reports **CC0: Public Domain**. The [source record](../../../data/provenance_AI_assisted/sources.json) pins the version-specific download URL and metadata snapshot hash |
| Byte-for-byte identity between Kaggle and the audited copy | **Verified by direct source comparison:** the [recorded online run](../../../data/provenance_AI_assisted/results/verification_20261118.json) on 2026-11-18 confirms identical bytes between the common raw CSV, the version-1 Kaggle archive member, and the GitHub CSV at commit `aa3faf512362f941721a85793e65baf5c3c7d760` |

The initial content audit measured the CSV; the complementary [provenance verifier](../../../data/provenance_AI_assisted/README.md) supplies executable source comparisons and bundled metadata. Its recorded online run passed **27 checks**, including direct byte comparisons with both public sources and verification of Kaggle metadata. These are provenance and storage assertions, separate from the statistical audit's 299 comparisons. Offline runs check the local CSV and historical metadata and explicitly mark external comparisons as not performed.

The snapshot records the publisher's statements at retrieval time. CC0 is the license reported by that metadata, not a conclusion inferred from the CSV; a matching hash identifies content without independently authenticating download origin. Online verification can detect subsequent source changes. A different adopted CSV requires recalculating the results. The common raw CSV is tracked in Git; [data/README.md](../../../data/README.md) explains access, verification commands, and the rules for additional raw or processed files.

---

## Annex A. Complete inventory of audited variables

Types reflect ordinary pandas CSV inference. Units suggested by field names are indicative, not a substitute for a validated data dictionary.

| Group | Column | Expected type | Missing | Observed range or categories | Field meaning |
| --- | --- | --- | ---: | --- | --- |
| Identification | `Participant_ID` | `object` | 0 | 1,000 IDs | Simulated participant key |
| Identification | `Day_Number` | `int64` | 0 | 1–30 | Within-participant day index |
| Demographics | `Age_Group` | `object` | 0 | 5 categories | Age group, not exact age |
| Demographics | `Gender` | `object` | 0 | 4 categories | Categorical gender |
| Demographics | `Occupation_Status` | `object` | 0 | 6 categories | Occupational status |
| Nicotine and craving | `Nicotine_Use_Duration_Months` | `int64` | 0 | 3–120 | Reported nicotine use duration, in months |
| Nicotine and craving | `Pouches_Per_Day` | `int64` | 0 | 0–24 | Daily nicotine pouch count |
| Nicotine and craving | `Pouch_Strength_mg` | `int64` | 0 | 4–15 | Concentration per pouch, in mg according to the name |
| Nicotine and craving | `First_Pouch_Time` | `object` | 0 | 37 HH:MM values | First pouch time, stored as text |
| Nicotine and craving | `Time_Since_Last_Pouch_Minutes` | `float64` | 355 | 5–716 | Minutes since last use |
| Nicotine and craving | `Longest_Nicotine_Free_Period_Hours` | `float64` | 380 | 1–23.9 | Longest nicotine-free interval, in hours |
| Nicotine and craving | `Morning_Cravings_Score` | `float64` | 369 | 0–10 | Morning craving score |
| Nicotine and craving | `Afternoon_Cravings_Score` | `float64` | 373 | 0–10 | Afternoon craving score |
| Nicotine and craving | `Evening_Cravings_Score` | `float64` | 346 | 0.4–10 | Evening craving score |
| Nicotine and craving | `Overall_Craving_Score` | `float64` | 349 | 0–10 | Overall craving score |
| Nicotine and craving | `Craving_Triggers` | `object` | 323 | 12 categories | Categorical craving trigger |
| Nicotine and craving | `Craving_Intensity_Peak` | `float64` | 0 | 0–10 | Peak intensity score |
| Nicotine and craving | `Craving_Duration_Minutes` | `int64` | 0 | 3–180 | Craving duration, in minutes |
| Nicotine and craving | `Attempted_To_Resist_Craving` | `object` | 345 | Yes / No | Reported attempt to resist craving |
| Nicotine and craving | `Successfully_Resisted` | `object` | 357 | Yes / No | Reported successful resistance |
| Psychology | `Daily_Anxiety_Score` | `float64` | 0 | 0–10 | Daily anxiety |
| Psychology | `Morning_Anxiety_Score` | `float64` | 0 | 0–10 | Morning anxiety |
| Psychology | `Evening_Anxiety_Score` | `float64` | 347 | 0–10 | Evening anxiety |
| Psychology | `Perceived_Stress_Score` | `float64` | 0 | 0–10 | Perceived stress |
| Psychology | `Mood_Score` | `float64` | 342 | 0–10 | Mood |
| Psychology | `Irritability_Score` | `float64` | 0 | 1–9.3 | Irritability |
| Psychology | `Restlessness_Score` | `float64` | 0 | 1.4–9 | Restlessness |
| Habits and activities | `Sleep_Duration_Hours` | `float64` | 0 | 3.5–11 | Hours of sleep |
| Habits and activities | `Sleep_Quality_Score` | `float64` | 0 | 3–10 | Sleep quality score |
| Habits and activities | `Caffeine_Intake_mg` | `int64` | 0 | 0–600 | Daily caffeine intake, in mg |
| Habits and activities | `Exercise_Minutes` | `float64` | 370 | 0–180 | Minutes of exercise |
| Habits and activities | `Screen_Time_Hours` | `float64` | 373 | 1–14 | Hours of screen time |
| Habits and activities | `Work_Or_Study_Hours` | `float64` | 0 | 0–18 | Hours of work or study |
| Habits and activities | `Major_Stress_Event_Today` | `object` | 0 | Yes / No | Indicator of a stressful event that day |
| Habits and activities | `Social_Interaction_Hours` | `float64` | 353 | 0–10 | Hours of social interaction |

### Interpretation and reproducibility notes

Results use the full CSV associated with the Git object above. Checks covered record and participant counts, missing fields, formats, distributions, and valid consecutive-day pairs. Types reflect inference compatible with a common CSV reader such as pandas; **no type declarations are attributed to Kaggle**. The file is comma-delimited text with one row per observation.

The [statistical audit guide](dataset_audit_AI_assisted/README.md) provides commands for a fresh reproduction in a separate output directory and independent validation. It also explains why the historical audit fingerprints the earlier Spanish source, while the English document and subsequent editorial revisions have a different document hash. This source-version difference does not alter the verified numerical findings; historical outputs and reference expectations remain preserved.

The additional correlation calculations are **descriptive**, not causal inference or validation of human behavior. No predictive model was fitted, and the correlations were not used to declare an experimental objective. Version and license statements rely on the bundled publisher metadata and executable provenance checks linked in section 1.9; the CSV alone establishes neither download origin nor licensing. The generation formula remains unverified.
