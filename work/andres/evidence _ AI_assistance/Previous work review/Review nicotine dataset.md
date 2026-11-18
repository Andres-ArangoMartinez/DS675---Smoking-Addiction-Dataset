# Review nicotine craving dataset

> User context
>
> Attachments:
> - Act as a research librarian, systematic literature reviewer, data scientist, an…: `C:/Users/Andres/.codex/attachments/e9ced058-fd08-4d4b-83dc-de4559d69f63/Pasted text.txt`

<details><summary>6 previous messages</summary>

> I’ll read the pasted request first, then work from its requirements and available sources.
>
> Revisaré primero la procedencia y los archivos del conjunto de Kaggle, y después contrastaré el repositorio indicado con estudios y conjuntos longitudinales relacionados. Distinguiré lo que pueda comprobar directamente de lo que solo esté descrito por sus autores.
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `"The Nicotine Craving and Anxiety Dynamics Dataset" synthetic ...`
>
> Searched the web for `"datascikhan" "nicotine" craving dataset github ...`
>
> Searched the web for `"nicotine" "pouch" "craving" "participant_id" dataset kaggle synthetic ...`
>
> </details>
>
> La evidencia ya muestra dos precedentes especialmente cercanos: un repositorio que declara trabajar con el mismo tema y EMASENS, que compara modelos grupales y personalizados. Estoy comprobando la identidad exacta de los archivos y si los resultados del repositorio están realmente ejecutados.
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `"Nicotine_Craving_Anxiety_Dynamics_30Days.csv" ...`
>
> Searched the web for `'execution_count'`
>
> Searched the web for `'kaggle'`
>
> </details>
>
> all in this chat soud be in e glish
</details>

# Literature and prior-work review: Nicotine Craving and Anxiety Dynamics

**Search date: November 10, 2026**

## 1. Executive summary

The strongest immediate precedent is [NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction), which analyzes a 30-day nicotine craving and anxiety dataset with a highly similar title and schema. Its notebook contains saved execution outputs and compares temporal models. However, **I could not verify that its CSV is byte-for-byte the Kaggle dataset**: neither the repository README nor the notebook cites the Kaggle URL, and the Kaggle data page was not readable through the available search tool. The connection is therefore **strong but unconfirmed**.

The repository’s reported results should not be treated as evidence of valid prospective forecasting without further investigation. Its code includes same-day predictors, such as evening craving measures, when predicting the daily craving score. In addition, its rolling-feature code and cross-validation design have problems that undermine the README’s claim of strictly leak-free temporal modeling. These observations are based on direct inspection of the [notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

The most relevant real-world scientific precedents are:

1. **EMASENS**, an intensive smoking-cessation study with repeated ecological momentary assessments and wearable sensors. Its researchers compared group, individual, and hybrid models. A later paper reused the same cohort to investigate measurement frequency, feature selection, and personalization. [Perski et al. (2024)](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000594); [Leppin et al. (2026)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0349028).
2. **Fisher and Soyster’s smoking study**, available through openESM, with repeated observations of craving, cigarette use, affect, stress, sleep, and social experience. [openESM record](https://openesmdata.org/datasets/0037_fisher/).
3. **Smoke Free app data**, used to classify lapses from self-initiated reports. This is a different cohort from EMASENS. [Perski et al. (2023)](https://pubmed.ncbi.nlm.nih.gov/36971111/).

For Milestone 2, a defensible contribution would be a **carefully defined next-day prediction task**, evaluated separately for previously observed participants and entirely unseen participants, with strict availability rules and simple baselines. This would be a useful methodological contribution to the project; **its novelty is not established**. Group versus personalized prediction, feature reduction, and comparisons of data-collection burden have already been studied in related research.

**Important provenance limitation:** I could not establish whether the Kaggle data are real, synthetic, or simulated. The publisher’s discussion links to the dataset but does not establish a study protocol or data-generation process. Do not describe the data as a verified clinical cohort—or as verified synthetic data—until the actual Kaggle documentation or publisher confirms its provenance. [Publisher’s Kaggle discussion](https://www.kaggle.com/general/739441).

### Evidence labels used below

- **Directly verified:** I inspected the linked source, code, or metadata.
- **Reported:** The source states the finding, but I did not independently reproduce it.
- **Inferred:** The conclusion follows from available evidence but is not explicitly established.
- **Unverified:** The required evidence was inaccessible or not found.

---

## 2. Kaggle dataset: identity, structure, and provenance

### What is established

**Directly verified:** The Kaggle discussion by **Shair Khan** explicitly links to the requested dataset and refers to it as *The Nicotine Craving & Anxiety Dynamics Dataset*. The discussion invites predictive modeling of craving, anxiety, and related distress. It does not, by itself, document the sampling protocol, instrument validation, generation procedure, or clinical provenance. [Kaggle discussion](https://www.kaggle.com/general/739441).

**Unverified:** The [Kaggle dataset page](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data) did not expose readable page content through the research tool. I could not inspect the original Kaggle CSV, full data dictionary, license, version history, or publisher’s complete description. Consequently, I cannot independently confirm its:

- File name, row count, column count, exact variable definitions, units, and missingness.
- Population, recruitment, consent, clinical setting, or sampling procedure.
- Status as real, synthetic, simulated, or a mixture.
- Relationship to the CSV described in the NumiKun repository.
- License or permission to redistribute.

### Candidate structure from the related repository

**Reported, not independently verified against Kaggle:** NumiKun describes a CSV named `Nicotine_Craving_Anxiety_Dynamics_30Days.csv` containing 30,000 records, 1,000 participants, 30 days per participant, and 35 original attributes. The notebook’s saved output also reports 30,000 rows and 1,000 participants. Examples named in the repository include:

- `Participant_ID`, `Day`
- `Overall_Craving_Score`, `Daily_Anxiety_Score`
- Morning, afternoon, evening, peak, and duration-related craving measures
- `Morning_Anxiety_Score`, `Evening_Anxiety_Score`
- `Restlessness_Score`, `Irritability_Score`, `Sleep_Quality_Score`
- `Caffeine_Intake_mg`, `Heart_Rate_BPM`
- `Time_Since_Last_Pouch_Minutes`, `Pouches_Per_Day_Reported`
- `Major_Stress_Event_Today`, `Perceived_Stress_Score`

These descriptions are useful for orientation but **should not yet be presented as a verified Kaggle codebook**. The repository’s language suggesting monitored participants and physiological measurements is also an author description, not independent evidence that observations came from real people or instruments. [Repository README](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/README.md); [notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

### Verification needed before modeling

Obtain the exact Kaggle version and preserve its original metadata. Then document:

1. Filename, version, download date, license, SHA-256, schema, and row count.
2. Unique participant IDs, days per ID, duplicates, missingness, value ranges, and categorical levels.
3. Definitions and timing of every candidate predictor and target.
4. Whether targets are calculated from other columns—for example, whether an overall craving score is a function of same-day morning, afternoon, and evening scores.
5. Whether the publisher documents synthetic generation, an actual study, or neither.
6. A hash and record-level comparison with the repository CSV.

A matching filename or similar schema would strengthen the connection; an identical file hash or matching records and schema would provide substantially stronger evidence.

---

## 3. Exact-dataset repositories and projects

### 3.1 NumiKun/Smoking-Addiction — highest-relevance candidate

**Identity: strongly related; exact match unverified.** The repository contains the candidate filename and a matching research topic. Its README and notebook do not contain the Kaggle URL, and I could not compare the files directly. The repository should therefore be cited as a **probable same-dataset precedent**, not yet a verified exact-dataset reuse. [README](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/README.md); [notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

**Executed or proposed?** The notebook contains execution counts, saved outputs, reported metrics, and an experiment summary. This directly establishes that execution output is present in the published notebook; I did **not** rerun the notebook or independently verify that its outputs were generated from the currently available files.

| Aspect | What the source reports or code shows |
|---|---|
| Targets | Continuous `Overall_Craving_Score` and `Daily_Anxiety_Score` for the record being modeled |
| Inputs | Original non-target columns plus lags, rolling statistics, ratios, and interactions |
| Models | Persistence baseline; Ridge, Lasso, ElasticNet, Random Forest, Gradient Boosting, HistGradientBoosting, XGBoost, LightGBM, and LSTM |
| Main split | Days 1–20 training, 21–25 validation, 26–30 test, across the same participant population |
| Preprocessing | Median imputation and standard scaling; README says parameters are fitted on training data |
| Metrics | MAE, RMSE, and \(R^2\); five-fold `TimeSeriesSplit` is also reported |
| Reported best craving test result | XGBoost: MAE 0.2350, RMSE 0.3022, \(R^2=0.9680\) |
| Reported best anxiety test result | LightGBM: MAE 0.3315, RMSE 0.4216, \(R^2=0.9546\) |

These are **author-reported results**, on daily score regression, for test days 26–30. They are not comparable to the lapse-classification AUCs in the studies below. The test appears to represent later records for participants whose earlier records were available, not a test on entirely new people. [README and metrics](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/README.md).

#### Critical code findings

1. **Same-day information changes the task.** The notebook builds its feature list by excluding the participant ID, day, and the two target columns, leaving other original columns as predictors. Thus same-day craving components can remain available when predicting the overall daily craving score. An evening measure cannot support a forecast made at the start of that day. If the overall score incorporates those components, the task may also approach reconstruction of the target. The latter formula has **not** been verified. [Notebook feature selection](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

2. **The rolling calculations are not grouped after shifting.** The code uses `g.shift(1).transform(lambda x: x.rolling(...))`. `g.shift(1)` returns a Series; the subsequent rolling operation is applied to that Series rather than separately to each participant’s group. Near participant boundaries, windows can incorporate shifted values from the preceding participant. The practical effect on metrics requires a reproducible test, but the code does not establish participant-isolated rolling windows. [Notebook feature engineering](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

3. **The cross-validation order does not represent a global forward timeline.** The notebook sorts by `[GROUP_COL, TIME_COL]` before applying `TimeSeriesSplit`. Consequently, a fold may train on later study days for earlier participants and test on earlier study days for later participants. That is different from holding out a later day across all participants. The code also transforms the data before cross-validation rather than fitting preprocessing independently within each fold, so fold-level preprocessing leakage is possible. [Notebook cross-validation](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

4. **Model-selection claims require care.** The README identifies best models using test results. If the test set was used to choose the winner, it no longer provides an untouched estimate for that selection. The extent of selection and any earlier experiments cannot be reconstructed from the README alone.

5. **High \(R^2\) is not a clinical result.** The values may reflect contemporaneous predictors, score construction, data-generation regularities, or other properties. They do not establish that a model can prospectively predict clinical outcomes.

### 3.2 Other exact-dataset work

**No additional exact-dataset repository, paper, or notebook was verified in the searches conducted.** Searches using the dataset title, Kaggle slug, publisher name, and candidate CSV filename did not establish another exact match. This is a bounded negative finding, not proof that no such work exists. Kaggle notebooks, unindexed code, private projects, and sources not searched directly remain possible.

---

## 4. Related datasets, ranked by relevance and accessibility

### 4.1 EMASENS: prompted EMA and wearable sensors

**Directly verified in the publication and archive:** This was a real-world, 10-day longitudinal smoking-cessation study. The study recruited 46 participants; 38 met the EMA adherence criterion, and 30 also met the sensor-data criterion. The protocol used 16 prompts per day. Surveys included craving, positive and negative affect, confidence and motivation to remain quit, bodily pain, social and physical context, cigarette availability, alcohol, caffeine, nicotine use, and participant-specific factors. Wearable data were also collected. [Perski et al. (2024)](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000594).

- **Unit:** Momentary survey and sensor observations, not a single daily row.
- **Product and target:** Cigarette smoking lapse during a quit attempt, not nicotine-pouch count or a daily anxiety score.
- **Access:** The [GitHub repository](https://github.com/OlgaPerski/EMASENS_ML) and [Zenodo v2.0.0 archive](https://zenodo.org/records/12532026) describe data and analytic code. The paper also links a [preregistered protocol](https://osf.io/ywqpv).
- **Format and license:** Zenodo provides a 3.3 MB ZIP of the repository release. I did not inspect each file, the detailed data dictionary, or a definitive reuse license; confirm those before reuse.
- **Important cohort relationship:** [Leppin et al. (2026)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0349028) explicitly state that their analysis extends the earlier work **using the same data**. Their 37-person analytic sample is not a separate independent dataset.

### 4.2 Fisher and Soyster smoking EMA dataset

**Directly verified through the harmonized dataset record:** [openESM’s Fisher (2019) record](https://openesmdata.org/datasets/0037_fisher/) describes 52 regular smokers, four randomly scheduled surveys per day, and maxima of 128 observations and 34 days. The 128 and 34 figures are **maximum observed time points and days**, not a total record count or a guarantee that every participant completed that schedule.

- **Unit:** Momentary survey; raw timestamps are reported as available.
- **Variables:** Cigarettes since the prior survey, current craving to smoke, restlessness, irritability, nervousness, stress, affect, sleep items, and positive social interactions.
- **Scales:** Many momentary ratings use 0–100 response scales. Sleep questions are morning-only, and some wording or coding is marked unclear by openESM.
- **Access:** Harmonized data via [Zenodo](https://doi.org/10.5281/zenodo.17348069) or the `openesm` R/Python packages; original source and code are linked at [OSF](https://osf.io/nkemg/). The record lists **CC BY-NC 4.0** for the harmonized data. Verify the terms applicable to any original files separately.
- **Study reference:** Fisher and Soyster, *Generating accurate personalized predictions of future behavior: A smoking exemplar* (2019), [preprint DOI](https://doi.org/10.31234/osf.io/e24v6). I did not inspect the full preprint or independently verify its exact algorithms and metrics.
- **Codebook caveat:** openESM links the [Soyster and Fisher (2019) EMA-design article](https://doi.org/10.1371/journal.pone.0217150) as a codebook reference. That article concerns survey design; it should not automatically be treated as a separate predictive evaluation.

### 4.3 Smoke Free app lapse reports

**Directly verified in the article abstract:** This real-world app dataset contains **37,002 self-initiated entries from 791 users**, with 7.6% of entries identified as lapses. Users included in the analysis had at least 20 unprompted entries. Reports included craving severity, mood, activity, and social context. The observation is an app entry, not a daily scheduled assessment. [Perski et al. (2023)](https://pubmed.ncbi.nlm.nih.gov/36971111/).

- **Access:** The associated [LSHTM Data Compass record](https://datacompass.lshtm.ac.uk/id/eprint/3694/) points to [Zenodo DOI 10.5281/zenodo.8423920](https://doi.org/10.5281/zenodo.8423920) for data and code. The LSHTM landing page itself has no files, and I could not inspect the Zenodo files, formats, license, or detailed codebook in this pass.
- **Limitation:** Self-initiated reports are selected by user behavior and may not represent all moments of risk or non-risk.

### 4.4 Smart-T2 smoking-cessation cohort

**Directly verified from the published abstract:** Hébert and colleagues analyzed 74 clinic participants asked to complete EMA five times daily for four weeks after their quit date. The outcome was time to first smoking lapse; 52 had an identified lapse and 22 were classified as non-lapsed at follow-up. The analysis used 31 EMA predictors and a treatment indicator. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/33092911/); [article text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496911/).

- **Unit:** Repeated EMA and time to first event.
- **Access:** The paper is accessible through PubMed Central. I did not verify an openly reusable participant-level dataset, code repository, or license.
- **Limitations:** Small, nonrepresentative treatment-seeking sample; the paper notes that lapse timing relied on self-report and was not biochemically verified.

I did not verify a public, longitudinal **nicotine-pouch-specific** dataset comparable to the Kaggle candidate in this search. That remains a worthwhile targeted search rather than a conclusion that such data do not exist.

---

## 5. Related scientific papers and predictive studies

### Perski et al. (2024): EMA, sensors, and personalized lapse classification

**Citation:** Perski et al., “Supervised machine learning to predict smoking lapses from Ecological Momentary Assessments and sensor data: Implications for just-in-time adaptive intervention development,” *PLOS Digital Health* (2024), [doi:10.1371/journal.pdig.0000594](https://doi.org/10.1371/journal.pdig.0000594).

This is an actual supervised-learning study, not just an association analysis. It evaluates group-level, individual-level, and hybrid algorithms, with and without sensor data. Without sensors, the best group model’s reported AUC was 0.899 for out-of-sample observations, but the median person-specific AUC for unseen individuals was 0.639. Individual models were feasible for only 15 of 38 participants. With sensors, the reported group AUC was 0.952 and the median AUC across unseen individuals was 0.745; individual models were feasible for 11 of 30 participants. [Paper](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000594).

**Interpretation:** Strong pooled discrimination did not ensure uniform performance for new individuals. Different analytic samples and event availability also limit simple comparisons between individual, hybrid, and group models. The paper is directly relevant to a participant-aware evaluation, but its momentary lapse classification is not equivalent to next-day pouch craving regression.

### Leppin et al. (2026): sampling burden, feature selection, and personalization

**Citation:** Leppin et al., “Optimising supervised machine learning algorithms predicting cigarette cravings and lapses for a smoking cessation just-in-time adaptive intervention (JITAI),” *PLOS One* (2026), [doi:10.1371/journal.pone.0349028](https://doi.org/10.1371/journal.pone.0349028).

Using the **same EMASENS cohort**, the authors analyzed 5,964 EMA responses from 37 participants and varied prompt frequency, feature count, target, and the amount of a participant’s own data used in training. Across configurations, they reported median ROC-AUC of 0.659 for lapse and 0.628 for high craving. Reducing features had little effect on lapse performance but slightly reduced craving performance in their comparison. More participant-specific training data improved some lapse F1 results, while effects varied by target and metric. [Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0349028).

**Implication:** Feature selection, burden/performance trade-offs, and hybrid personalization are existing research ideas. They can still be valuable project analyses, but cannot be claimed as generally novel.

### Perski et al. (2023): self-initiated app reports

**Citation:** Perski et al., “Classification of Lapses in Smokers Attempting to Stop: A Supervised Machine Learning Approach Using Data From a Popular Smoking Cessation Smartphone App,” *Nicotine & Tobacco Research* (2023), [doi:10.1093/ntr/ntad051](https://doi.org/10.1093/ntr/ntad051).

The authors trained group, individual, and hybrid classifiers on the 791-user app dataset. They reported a pooled group AUC of 0.969, but individual out-of-sample AUCs ranged from 0.482 to 1.000. Individual-level models could be constructed for 39 users, and hybrid models for 184. This is **classification of lapse versus non-lapse reports**; do not assume the figure represents prediction of a future lapse before the report. [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/36971111/).

### Hébert et al. (2021): time to first smoking lapse

**Citation:** Hébert ET, Suchting R, Ra CK, Alexander AC, Kendzor DE, Vidrine DJ, and Businelle MS. “Predicting the first smoking lapse during a quit attempt: A machine learning approach,” *Drug and Alcohol Dependence* 218:108340 (2021), [doi:10.1016/j.drugalcdep.2020.108340](https://doi.org/10.1016/j.drugalcdep.2020.108340).

The authors used Cox models and elastic-net selection to examine time to first lapse. Five retained predictors included perceived likelihood of smoking that day, confidence, motivation, urge, and cigarette availability. The reduced model did not adequately approximate the fuller non-penalized model. This is a useful example of **exploratory survival modeling and feature selection**, but the abstract does not establish a comparable external held-out predictive benchmark. [PubMed](https://pubmed.ncbi.nlm.nih.gov/33092911/); [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496911/).

### Fisher and Soyster (2019): personalized prediction

**Citation:** Fisher AJ and Soyster PD. “Generating accurate personalized predictions of future behavior: A smoking exemplar” (2019), [doi:10.31234/osf.io/e24v6](https://doi.org/10.31234/osf.io/e24v6).

The linked openESM dataset makes this a close precedent for participant-specific prediction from repeated smoking and affect measures. **Unverified in this review:** the full preprint’s precise target, model specification, split, and numerical results. Those should be checked in the full text and associated [OSF materials](https://osf.io/nkemg/) before drawing a detailed novelty comparison. [openESM record](https://openesmdata.org/datasets/0037_fisher/).

---

## 6. Variable-by-variable comparison

“Related” means a construct has some overlap; it does **not** mean that scales, timing, or instruments are interchangeable.

| Construct | Kaggle / candidate repository | Fisher / openESM | EMASENS | Smoke Free app |
|---|---|---|---|---|
| Participant and time | Candidate: ID and study day; Kaggle file unverified | ID, day, beep, timestamps | Repeated prompted and event-contingent records | Self-initiated app entries |
| Nicotine product and use | Candidate: pouches per day and time since last pouch | Cigarettes since previous survey | Cigarette lapse; nicotine use also reported | Cigarette lapse reports |
| Craving | Candidate: overall and time-of-day scores | Current urge to smoke, 0–100 | Momentary craving severity; later study also models high craving | Craving severity at app entry |
| Anxiety / nervousness | Candidate: daily and morning/evening anxiety scores | Momentary nervousness, 0–100; not a validated equivalent of daily anxiety | Negative-affect items, including stress; not automatically the same anxiety scale | Mood reported; exact anxiety item unverified |
| Stress | Candidate: perceived score and major stress event | Current stress, 0–100 | Negative affect and context | Mood/context; exact stress measure unverified |
| Irritability / restlessness | Candidate: separate scores | Momentary `irritable` and `restless`, 0–100 | Specific equivalent items not verified in this pass | Specific items not verified |
| Sleep | Candidate: sleep quality | Morning-only sleep difficulty and duration; wording partly uncertain | Comparable sleep item not verified | Not verified |
| Social context | Candidate described by the project prompt; Kaggle column unverified | Enjoyment of social interactions | Social context captured | Social context captured |
| Caffeine | Candidate: mg | Not established from reviewed record | Caffeine consumption reported | Not verified |
| Sensor / physiology | Candidate README names heart rate; collection method unverified | No passive sensors per openESM | Wearable sensor data | Not verified |
| Time horizon | Candidate: person-day; true measurement times unclear | Several momentary observations per day | High-density momentary observations for 10 days | Irregular self-initiated events |

Sources: [candidate README](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/README.md), [Fisher codebook](https://openesmdata.org/datasets/0037_fisher/), [EMASENS paper](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000594), and [app study](https://pubmed.ncbi.nlm.nih.gov/36971111/).

### Compact methods comparison

| Source | Data type and population | Task and horizon | Evaluation / reported result | Access and relevance |
|---|---|---|---|---|
| NumiKun | Candidate 30,000 person-days; provenance unclear | Daily craving and anxiety regression; includes same-day inputs | Days 26–30 for previously represented participants; reported craving \(R^2=0.968\), anxiety \(R^2=0.9546\); leakage concerns above | Code and saved outputs open; exact Kaggle identity unverified |
| EMASENS, 2024 | Real smokers; 38 EMA-eligible, 30 sensor-eligible | Momentary lapse classification | Group and per-person evaluation; pooled and person-specific AUC differ substantially | [Data/code archive](https://zenodo.org/records/12532026); very relevant to validation design |
| EMASENS, 2026 | Same cohort; 37-person analysis | High craving and lapse; momentary, across configurations | Random Forest; feature count, sampling frequency, and own-data comparisons | [Paper and linked materials](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0349028); very relevant to ablation |
| Fisher | Real regular smokers; 52 | Personalized smoking prediction; exact horizon and metrics not checked here | Requires full-preprint inspection | [openESM](https://openesmdata.org/datasets/0037_fisher/); strong variable overlap |
| Smoke Free app | Real app users; 791, 37,002 entries | Lapse versus non-lapse report classification | Group and participant-specific AUC; self-initiated data | [Data record](https://datacompass.lshtm.ac.uk/id/eprint/3694/); strong model-comparison precedent |
| Smart-T2 | Real clinic cohort; 74 | Time to first smoking lapse | Cox and elastic-net feature selection; external predictive performance not established here | [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496911/); useful survival-analysis precedent |

---

## 7. Critical assessment of methods and evaluation

### Define the prediction moment first

A “daily” row can contain information collected at different times. If a model is intended to forecast tomorrow’s craving at the end of today, only data genuinely available by that cutoff should be used. If a model uses tomorrow evening’s craving component to estimate tomorrow’s overall craving, it answers a different question.

A target constructed from other fields creates an additional issue: even if the component scores are available before the daily score is calculated, an accurate model may mainly reconstruct a formula. Establishing the target’s construction is therefore as important as avoiding obvious chronological leakage.

### Distinguish two generalization questions

- **Known-participant forecasting:** Can a model predict later days for people whose earlier data are available? Use forward temporal splits within each participant and define which previous outcomes are observable at inference time.
- **New-participant generalization:** Can it predict for a person excluded entirely from model fitting and tuning? Hold out participant IDs; ensure feature engineering does not cross participants.

A third, hybrid question can allow an initial “warm-up” period from a new participant. Its results must be labeled separately because the model receives information about the test participant. EMASENS and the Smoke Free study have already investigated versions of these distinctions.

### Fit transformations inside the correct training fold

Imputation, encoding, scaling, feature selection, class rebalancing, and hyperparameter tuning should use only the relevant training partition. Lag and rolling calculations must be grouped by participant and use only observations available before the prediction cutoff. Check boundary cases explicitly.

For a panel dataset, applying a standard row-level `TimeSeriesSplit` to data sorted by participant ID does not automatically preserve global chronology. Splits should be constructed around the intended deployment question, not merely around row order.

### Metrics and uncertainty

For continuous scores, report MAE and RMSE in score units, with a persistence baseline and per-participant error distributions. For a classification task, report prevalence, precision–recall AUC, sensitivity, specificity, calibration, and a threshold-selection procedure, alongside ROC-AUC where useful. Confidence intervals should respect participant clustering.

Do not compare the NumiKun regression \(R^2\) to EMASENS lapse AUCs: the outcome, population, prediction moment, and evaluation units differ.

### Other material limitations

- **Synthetic or unclear provenance:** Strong performance may reflect generation rules rather than human behavior. Results cannot establish clinical validity.
- **Missingness:** Determine whether missing observations mean nonresponse, no event, or unavailable measurement.
- **Imbalance:** A rare high-craving threshold can make accuracy misleading.
- **Interpretability:** Feature importance describes model behavior under a particular dataset and can be unstable with correlated inputs. It does not establish that a feature causes craving or anxiety.
- **External validity:** Even a clean internal split does not demonstrate performance in real people, other products, or other settings.

---

## 8. Implications for Milestone 2

### Recommended task to investigate

**Candidate primary question:** At the end of day \(t\), can information available through that day predict `Overall_Craving_Score` for day \(t+1\)?

This is conditional on verifying that the target exists in the actual Kaggle version, that day ordering is meaningful, and that the variables’ collection times are documented. Define the cutoff and target before examining test performance.

A reproducible evaluation could include:

1. **Baselines:** Last observed craving, training-set mean, and a regularized linear model.
2. **Main models:** One interpretable regularized model and one tree-based model, rather than assuming that more architectures imply a stronger study.
3. **Two test settings:** Later days for known participants and held-out participants. If a warm-up period is allowed for the latter, report it as a separate hybrid setting.
4. **Feature-group comparison:** History alone; history plus sleep and mood; then history plus behavior and context. Use the same splits and assess whether added groups improve out-of-sample performance.
5. **Participant-level reporting:** Overall and per-person errors, uncertainty clustered by participant, and an audit of participants with few usable observations.
6. **Sensitivity analysis:** Exclude ambiguous same-day variables; test whether results change when suspected target components are removed.

This could yield a clear contribution **within the course project**: a transparent comparison of information available at prediction time and generalization to different participant populations. It would also directly address weaknesses observed in the candidate repository. It should not yet be advertised as a new clinical prediction method or an unprecedented research idea.

### What would be needed before claiming novelty

- Verify the Kaggle CSV’s identity, provenance, license, and generation method.
- Compare it directly with NumiKun’s CSV and reproduce the relevant baseline under identical and corrected conditions.
- Review the full Fisher preprint and its code, not only the dataset record.
- Search Kaggle notebooks and code-search indexes using the verified filename, column names, and dataset identifiers.
- Conduct targeted citation chaining for temporal participant-aware validation, feature-group ablation, and nicotine-pouch prediction.
- Specify the exact novelty claim: dataset, target, forecast horizon, inputs available at cutoff, population, and evaluation design.

A reasonable preliminary claim is: **“We evaluate a leakage-aware next-day prediction protocol on this dataset and compare known- and unseen-participant settings.”** Whether that protocol is novel remains unresolved.

---

## 9. Search method, limitations, and unresolved questions

**Approach:** I used exact-title and Kaggle-slug searches, the publisher name, the candidate CSV filename, the named GitHub repository, and targeted searches for EMA smoking-lapse prediction, personalized models, and the specified datasets. I followed references from the resulting publication, institutional repository, PubMed, Zenodo, openESM, and GitHub records. I inspected the NumiKun README and notebook code and saved outputs, as well as primary publication text and dataset metadata where available.

**Inclusion criteria:** Sources were prioritized when they documented the candidate dataset, a longitudinal nicotine/tobacco dataset with overlapping constructs, or an actual predictive model with relevant repeated-measures evaluation. Topic similarity alone was not treated as evidence of dataset identity.

**Practical limitations:**

- The Kaggle data page and API metadata were not readable through the available web tool; the original CSV and full documentation were not inspected.
- The exact NumiKun-to-Kaggle match was not established by hash or records.
- The Fisher preprint, individual archive files, detailed EMASENS codebook, and all reuse licenses were not fully audited.
- This was a targeted, multi-source search—not a registered systematic review or an exhaustive search of every requested platform. I did not conduct separate, comprehensive searches inside GitLab, Hugging Face, Figshare, Europe PMC, Crossref, Google Scholar, and Semantic Scholar. Their absence from the findings should not be read as a negative search result.
- No independent model execution or numerical reproduction was performed.

**Highest-priority unresolved questions:** Is the Kaggle data synthetic? How are the daily targets constructed? Are same-day fields timestamped? Does the repository CSV match the Kaggle version? What license applies? Without these answers, the precise predictive task and any clinical interpretation remain provisional.

---

## 10. Linked bibliography

### Primary research and study documentation

- [Perski et al. (2024), *Supervised machine learning to predict smoking lapses from Ecological Momentary Assessments and sensor data*](https://doi.org/10.1371/journal.pdig.0000594).
- [Leppin et al. (2026), *Optimising supervised machine learning algorithms predicting cigarette cravings and lapses*](https://doi.org/10.1371/journal.pone.0349028).
- [Perski et al. (2023), *Classification of Lapses in Smokers Attempting to Stop*](https://doi.org/10.1093/ntr/ntad051).
- [Hébert et al. (2021), *Predicting the first smoking lapse during a quit attempt*](https://doi.org/10.1016/j.drugalcdep.2020.108340).
- [Fisher and Soyster (2019), *Generating accurate personalized predictions of future behavior: A smoking exemplar*](https://doi.org/10.31234/osf.io/e24v6).
- [Soyster and Fisher (2019), *Involving stakeholders in the design of ecological momentary assessment research*](https://doi.org/10.1371/journal.pone.0217150).

### Datasets and repositories

- [Requested Kaggle dataset](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data).
- [NumiKun/Smoking-Addiction repository](https://github.com/NumiKun/Smoking-Addiction) and its [executed notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).
- [EMASENS GitHub repository](https://github.com/OlgaPerski/EMASENS_ML) and [Zenodo v2.0.0 archive](https://zenodo.org/records/12532026).
- [Fisher (2019) harmonized dataset and variable metadata](https://openesmdata.org/datasets/0037_fisher/); [original OSF materials](https://osf.io/nkemg/).
- [Smoke Free app data and code record](https://datacompass.lshtm.ac.uk/id/eprint/3694/).

### Publisher and contextual source

- [Shair Khan’s Kaggle discussion linking to the requested dataset](https://www.kaggle.com/general/739441).

> User context
>
> Attachments:
> - Este segundo prompt está orientado a **descubrir y organizar categorías de ante…: `C:/Users/Andres/.codex/attachments/5a90f42f-efda-4159-9259-296f721815fd/Pasted text.txt`

<details><summary>4 previous messages</summary>

> I’ll read the new request and use the previous review as context, keeping everything in English.
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `"Nicotine_Craving_Anxiety_Dynamics_30Days.csv" dataset synthetic kaggle ...`
>
> </details>
>
> A new and particularly relevant precedent has emerged: a 2026 study predicts next-day cigarette consumption from daily craving, mood, stress, and anxiety. I’m checking its validation design and tracing whether the associated studies reuse the same participants.
>
> <details><summary>Searched the web</summary>
>
> Searched the web for `machine learning leakage clinical longitudinal data patient overlap evaluation temporal split Kapoor Narayanan leakage reproducibility ...`
>
> Searched the web for `'participants'`
>
> Searched the web for `"Rapid and reliable computational markers" smoking 2026 participants authors ...`
>
> Searched the web for `"McKinty" "Reed" "2023" "2025" craving same sample daily nondaily anxiety ...`
>
> </details>
</details>

# Evidence map and taxonomy of prior work on nicotine craving, anxiety, and prediction

**Search date: November 10, 2026**

## 1. Executive summary

The literature supports organizing this project around four distinct questions:

1. **What is being predicted?** Craving, cigarette consumption, lapse, relapse, and anxiety are different outcomes.
2. **When is the prediction made?** Estimating a current state from contemporaneous data differs from forecasting the next day or the next smoking episode.
3. **For whom should the model generalize?** Performance on later observations from known participants differs from performance on entirely new participants.
4. **What kind of evidence supports the data?** Real-world EMA studies, controlled laboratory studies, and data of unknown provenance have different implications.

A particularly close precedent is [Lee et al. (2026)](https://doi.org/10.1038/s41386-026-02448-5), which modeled **next-day cigarette consumption** using daily craving, smoking, mood, stress, anxiety, and other measures. The authors compared standard cross-validation with a more explicitly time-aware analysis. This means that a proposal to predict next-day nicotine-related behavior from daily psychological measures would have a clear scientific antecedent.

The strongest candidate repository for the Kaggle dataset remains [NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction). It analyzes a dataset with a highly similar title and structure, and its notebook contains saved execution results. **Its use of the exact Kaggle file is still unverified**: I could not compare the files or find a direct Kaggle citation in the repository’s README or notebook.

The most useful methodological precedent is the **EMASENS** research program. It compares group-level, individual-level, and hybrid models and examines the effect of reducing measurement frequency and predictor count. Two important EMASENS papers use the **same cohort**, so they should not be counted as independent datasets. [Perski et al. (2024)](https://doi.org/10.1371/journal.pdig.0000594); [Leppin et al. (2026)](https://doi.org/10.1371/journal.pone.0349028).

The requested Kaggle dataset’s **provenance remains unknown**. I could not establish whether it contains observations from real participants, synthetic records, or simulated data. This uncertainty limits any claims about clinical relevance, external validity, or even the interpretation of a participant ID.

**Research-positioning conclusion:** There are several defensible directions for a graduate project, particularly a transparent comparison of forecast definitions and participant-aware evaluation. They are **candidates for investigation**, not established novel contributions. The exact task, horizon, predictors, and evaluation protocol remain open.

### Evidence labels

- **Directly verified:** Source text, metadata, or code was inspected.
- **Reported:** A result or dataset property is stated by the source but was not independently reproduced.
- **Inferred:** A reasoned interpretation of the available evidence.
- **Unverified:** Evidence was not accessible or was not found.

---

## 2. Verified description of the Kaggle dataset

### Identity

**Directly verified:** A [Kaggle discussion by Shair Khan](https://www.kaggle.com/general/739441) links to the requested dataset and calls it *The Nicotine Craving & Anxiety Dynamics Dataset*. The post discusses craving, anxiety, nicotine use, and potential predictive questions.

The [Kaggle dataset page](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data) did not expose readable dataset contents through the search interface used here. The publisher’s discussion is evidence that the dataset exists and is being promoted for analysis; it is **not sufficient documentation of a clinical study or data-generation process**.

### Candidate structure, not yet verified against Kaggle

The [NumiKun repository](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/README.md) reports a CSV called `Nicotine_Craving_Anxiety_Dynamics_30Days.csv`, with:

- 30,000 records;
- 1,000 participant identifiers;
- 30 days per participant;
- 35 original attributes;
- daily craving and anxiety targets, plus behavioral and contextual features.

The notebook’s saved output also reports 30,000 records and 1,000 participants. These are **reported properties of the repository’s candidate file**, not independently confirmed properties of the exact Kaggle version. [Notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

### Provenance and structure still unresolved

I could not independently verify:

- Whether the Kaggle data are **real, synthetic, simulated, or mixed**.
- The complete schema, data dictionary, units, scale ranges, or missingness.
- Whether daily scores are calculated from other columns.
- Whether records were actually collected at the times implied by their names.
- Recruitment, participant characteristics, setting, or follow-up procedures.
- License, version, file hash, or identity with NumiKun’s CSV.

**Practical implication:** Until those points are resolved, describe the file as a dataset of **unknown provenance**, and treat the reported person-day structure as provisional.

---

## 3. Search strategy and limitations

This is a **structured research search**, not a formal systematic review. It does not have a registered protocol, exhaustive database coverage, independent screening by multiple reviewers, or a reproducible record of all search-result counts.

### Platforms and materials actually consulted

I used web search to identify and inspect:

- Kaggle dataset and publisher discussion;
- GitHub README and notebook code;
- PubMed and PubMed Central records;
- PLOS and other publisher pages;
- openESM;
- Zenodo and OSF landing pages;
- university and institutional repositories;
- the author-linked GitHub repository for a newly identified daily-smoking study.

Representative searches included:

- `"Nicotine_Craving_Anxiety_Dynamics_30Days.csv" dataset synthetic kaggle`
- `"the-nicotine-craving-and-anxiety-dynamics-dataset" synthetic`
- `nicotine craving anxiety state daily nondaily nicotine users`
- `smoking craving prediction ecological momentary assessment temporal validation`
- `machine learning leakage clinical longitudinal data patient overlap`
- `sleep smoking craving ecological momentary assessment`
- `nicotine pouch pharmacokinetics craving randomized crossover`

### Screening and citation chaining

Sources were prioritized when they directly addressed at least one of:

- the candidate dataset;
- repeated nicotine, tobacco, craving, anxiety, affect, sleep, or contextual measurements;
- an explicitly defined predictive task;
- participant-level or temporal validation;
- methods for leakage or synthetic-health-data evaluation.

I followed the EMASENS publication to its dataset and code archive and then to the later paper explicitly reusing the cohort. I also followed the daily-smoking prediction paper to its [code and data repository](https://github.com/CCS-Lab/SmokingPred_ADO).

**Counts:** The number of records screened is not reliably available and is not estimated here.

**Access limitations:** The Kaggle file and full metadata were not inspected. Some publisher pages were inaccessible directly, although indexed article text, PubMed, or available full-text records supplied relevant details. I did not conduct separate exhaustive searches within Scopus, Web of Science, Google Scholar, Semantic Scholar, GitLab, Figshare, or Hugging Face. Therefore, “not found” below means **not found in this search**, not that no source exists.

---

## 4. Proposed taxonomy of related work

The categories below are based on the roles sources actually play in the project. A paper may have one primary category and several secondary connections.

### Category A — Candidate exact-dataset analyses

**Definition:** Public analyses that appear to use the Kaggle data or a file with a closely matching title and schema.

- **Typical questions:** Can daily craving or anxiety scores be modeled from the available columns?
- **Representative source:** [NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction).
- **Overlap:** Candidate file name, 30-day structure, craving and anxiety targets.
- **Boundary:** The repository does not establish that its file is identical to the requested Kaggle version.
- **Relevance: High**, because it may be the closest direct technical precedent.
- **Gap:** Hash, records, provenance, and code-level reproduction are needed.

### Category B — Daily and near-term prediction of use or craving

**Definition:** Models that predict nicotine-related behavior or estimate craving using information collected over time.

- **Typical outcomes:** Next-day cigarette count, high craving, or momentary craving state.
- **Representative sources:** [Lee et al. (2026)](https://doi.org/10.1038/s41386-026-02448-5); [Chatterjee et al. (2016), *mCrave*](https://doi.org/10.1145/2971648.2971672).
- **Overlap:** Repeated measures, craving, stress, mood, and temporal modeling.
- **Boundary:** Cigarette count is not pouch use; minute-level sensor estimation is not daily forecasting.
- **Relevance: High** for selecting a target and prediction horizon.
- **Gap:** None of these sources establishes results for the Kaggle dataset.

### Category C — Smoking cessation, lapse, and relapse

**Definition:** Studies of smoking after a quit attempt, including classification of a reported lapse or prediction of time to first lapse.

- **Typical outcomes:** Lapse versus non-lapse, time to first lapse, or cessation at follow-up.
- **Representative sources:** [Perski et al. (2024)](https://doi.org/10.1371/journal.pdig.0000594); [Perski et al. (2023)](https://doi.org/10.1093/ntr/ntad051); [Hébert et al. (2021)](https://doi.org/10.1016/j.drugalcdep.2020.108340).
- **Overlap:** Craving, stress, affect, nicotine use, and repeated behavior.
- **Boundary:** A lapse requires a defined quit attempt and event; a daily craving score alone is not a lapse or relapse measure.
- **Relevance: High** if a comparable outcome exists; otherwise medium as methodological background.
- **Gap:** The Kaggle file’s cessation status and outcome definitions are unverified.

### Category D — Psychological and behavioral dynamics

**Definition:** Studies examining associations among nicotine use, craving, affect, anxiety, and stress, including differences across and within individuals.

- **Typical questions:** Is anxiety associated with craving? Do affect–smoking relationships differ by person?
- **Representative sources:** [McKinty et al. (2026)](https://doi.org/10.1016/j.addbeh.2025.108501); [Spillane and Soyster (2023)](https://doi.org/10.1080/10826084.2023.2257312); [Reed et al. (2023)](https://doi.org/10.1016/j.addbeh.2023.107803).
- **Overlap:** Anxiety, negative affect, craving, and use.
- **Boundary:** Statistical associations, including lagged associations, do not automatically demonstrate out-of-sample predictive performance or causation.
- **Relevance: High** for motivating variables and interpreting their limits.
- **Gap:** Instruments and measurement times differ from the candidate dataset.

### Category E — Sleep, context, and product-specific mechanisms

**Definition:** Work on sleep, social context, stressors, or product-specific nicotine delivery that may affect the interpretation of candidate features.

- **Representative sources:** [Freeman and Gottfredson (2018)](https://doi.org/10.1016/j.addbeh.2017.11.001); [nicotine-pouch crossover study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9217727/); [sleep and smoking study protocol](https://doi.org/10.1371/journal.pone.0334129).
- **Overlap:** Sleep, craving, product use, and context.
- **Boundary:** The sleep study involves people in treatment for substance-use disorders, not necessarily nicotine-specific craving. A laboratory pouch study is not a daily ML prediction study. The 2025 sleep-and-smoking paper is a **protocol**, not completed results.
- **Relevance: Medium** for variable definitions and product differences.
- **Gap:** Evidence directly connecting a specific Kaggle column to a validated instrument is absent.

### Category F — Personalized, group, and hybrid models

**Definition:** Comparisons between models trained across people, for individual people, or on pooled data augmented with a participant’s own history.

- **Representative sources:** [Perski et al. (2024)](https://doi.org/10.1371/journal.pdig.0000594); [Leppin et al. (2026)](https://doi.org/10.1371/journal.pone.0349028); [Fisher and Soyster dataset](https://openesmdata.org/datasets/0037_fisher/).
- **Overlap:** Repeated observations and the question of individual versus population generalization.
- **Boundary:** A model that receives a participant’s early history answers a different question from one applied to a completely unseen person.
- **Relevance: High** for evaluation design.
- **Gap:** Individual models may be infeasible with short histories or few outcome events.

### Category G — Validation, leakage, and synthetic-data utility

**Definition:** Methodological work on the validity of ML evaluation and, conditionally, the use of synthetic health data.

- **Representative sources:** [Kapoor and Narayanan, *Leakage and the reproducibility crisis in machine-learning-based science*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/); [label-leakage framework](https://pubmed.ncbi.nlm.nih.gov/37669138/); [synthetic patient-data fidelity, privacy, and utility](https://pmc.ncbi.nlm.nih.gov/articles/PMC12059695/).
- **Overlap:** Feature availability, repeated measurements, evaluation, and provenance.
- **Boundary:** Synthetic-data methodology is **conditional background** until the Kaggle provenance is verified.
- **Relevance: High** for validation; contextual for synthetic-data assessment at present.
- **Gap:** General guidance does not replace an audit of the actual dataset and task.

---

## 5. Evidence map and comparison matrix

**Relationship codes:**
**A** = candidate exact-dataset work; **B** = overlapping data/variables; **C** = related target; **D** = association or mechanism; **E** = method/evaluation.

| Source | Category; population and product | Relevant variables | Outcome / horizon | Method and validation | Data/code and relationship |
|---|---|---|---|---|---|
| [NumiKun, undated repository](https://github.com/NumiKun/Smoking-Addiction) | A; candidate 1,000 IDs, 30 days; pouch-related fields reported; provenance unknown | Daily craving, anxiety, stress, sleep, use | Same-record daily craving/anxiety regression; predictor timing must be audited | Multiple regressors; days 1–20/21–25/26–30; saved output present; code concerns below | Repository open; Kaggle identity **unverified**. **A, B, C, E** |
| [Lee et al., 2026](https://doi.org/10.1038/s41386-026-02448-5) | B/F; 79 real cessation-clinic participants; cigarettes; 5–6 weeks | Smoking, craving, stress, mood, anxiety, cognitive tasks | Next-day cigarette count and end-of-treatment cessation | Time-lagged mixed-effects models; standard and forward-chaining CV | [Code and data repository](https://github.com/CCS-Lab/SmokingPred_ADO), as linked by paper. **B, C, E** |
| [Perski et al., 2024](https://doi.org/10.1371/journal.pdig.0000594) | C/F; EMASENS; 38 EMA-eligible, 30 sensor-eligible; cigarettes; 10 days | Craving, affect, context, nicotine use, sensors | Lapse classification using EMA and sensor information | Group, individual, and hybrid models; out-of-sample observation and individual evaluations | [Zenodo](https://zenodo.org/records/12532026), [GitHub](https://github.com/OlgaPerski/EMASENS_ML). **B, C, E** |
| [Leppin et al., 2026](https://doi.org/10.1371/journal.pone.0349028) | B/C/F; **same EMASENS cohort**, 37-person analysis | Craving, affect, context, measurement frequency | High craving and lapse; momentary classification | Random Forest; prompt-frequency, feature-selection, and personalization comparisons | [Study materials](https://github.com/OlgaPerski/EMASENS_ML). **B, C, E** |
| [Perski et al., 2023](https://doi.org/10.1093/ntr/ntad051) | C/F; Smoke Free app; 791 users, 37,002 entries; cigarettes | Craving, mood, activity, social context | Lapse versus non-lapse **reports** | Group, individual, hybrid classifiers; separate participant analyses | [Data and code record](https://datacompass.lshtm.ac.uk/id/eprint/3694/); files not inspected here. **B, C, E** |
| [Fisher and Soyster, 2019](https://openesmdata.org/datasets/0037_fisher/) | D/F; 52 regular smokers; up to 34 days; cigarettes | Momentary craving, use, stress, nervousness, restlessness, sleep, social interaction | Personalized smoking prediction; exact preprint target/horizon not checked | Full methods and results need direct inspection | [Harmonized data](https://doi.org/10.5281/zenodo.17348069); [OSF](https://osf.io/nkemg/). **B, E** |
| [Hébert et al., 2021](https://doi.org/10.1016/j.drugalcdep.2020.108340) | C; 74 clinic participants; cigarettes; four weeks | Urge, motivation, confidence, cigarette availability | Time to first lapse | Cox and elastic-net selection; out-of-sample benchmark not established here | [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8496911/); data/code availability unverified. **B, C** |
| [Chatterjee et al., 2016](https://doi.org/10.1145/2971648.2971672) | B; 61 cessation-study participants; cigarettes | Sensor-derived stress and self-reported craving | Minute-level craving estimation | Conditional random-field approach; leave-one-participant-out evaluation | [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5161415/); code/data availability unverified. **C, E** |
| [McKinty et al., 2026](https://doi.org/10.1016/j.addbeh.2025.108501) | D; 114 adults; daily and non-daily nicotine/tobacco users | State anxiety, craving, VR cues | Pre- and post-cue craving association | Laboratory association analysis; not an out-of-sample forecasting benchmark | Data available on request per publisher. **B, D** |
| [Freeman and Gottfredson, 2018](https://doi.org/10.1016/j.addbeh.2017.11.001) | E; 122 people in substance-use treatment | Sleep quality, craving, willpower | Temporal sleep–craving associations | Multilevel EMA analysis, four surveys/day for three weeks | [PubMed](https://pubmed.ncbi.nlm.nih.gov/29137841/); data/code unverified. **B, D** |
| [Kapoor and Narayanan, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/) | G; methodological review across ML science | Leakage during collection, preprocessing, modeling, evaluation | Not a nicotine prediction task | Taxonomy and documented examples | Open article. **E** |

### Cohort clusters and uncertainty

- **Confirmed same cohort:** Perski 2024 and Leppin 2026 both use EMASENS; Leppin explicitly says it extends the earlier analysis using the same data.
- **Separate cohort:** The 791-user Smoke Free app dataset is a separate source from the prompted EMASENS study.
- **Possible overlap, not established:** [Reed et al. (2023)](https://doi.org/10.1016/j.addbeh.2023.107803) and [McKinty et al. (2026)](https://doi.org/10.1016/j.addbeh.2025.108501) both describe samples of 80 daily and 34 non-daily users and related cue-reactivity research. Those similarities are **not sufficient to confirm identical participants**. Check the original study identifiers and recruitment descriptions before counting them as independent cohorts.
- **Fisher/openESM and Spillane–Soyster:** The participant count and authorship make a relationship plausible, but I did not verify the underlying cohort identity. Treat them separately until the study materials confirm reuse.

---

## 6. Detailed review of the strongest sources

### 6.1 Candidate repository: what has and has not been done

[NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction) reports models for `Overall_Craving_Score` and `Daily_Anxiety_Score`. Its notebook contains saved outputs and lists linear models, tree ensembles, boosting methods, an LSTM, and a persistence baseline.

**Reported test results:** For days 26–30, the README reports craving \(R^2=0.9680\) with XGBoost and anxiety \(R^2=0.9546\) with LightGBM. These are **not independently reproduced**. They do not establish future-day predictive accuracy because the feature set includes other same-record variables and its temporal availability has not been established. [README](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/README.md).

**Direct code observations:**

- The code excludes the participant ID, day, and two target columns when building the feature list; other original columns remain candidates. Some may describe the same day or be components of a daily score.
- Lag values are grouped by participant, but the rolling calculation follows `groupby(...).shift(1)` with a rolling operation on the resulting Series. This can allow a rolling window near one participant’s boundary to include values from another participant.
- The cross-validation code sorts by participant and day before applying `TimeSeriesSplit`, so it is not a global forward split by study day. The preprocessing transformation is also performed before cross-validation rather than being fitted separately inside each fold.

These are **code-review findings**, not a reproduced estimate of the magnitude of bias. See the [notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb).

### 6.2 Lee et al. (2026): the closest daily forecasting precedent

**Citation:** Lee J-H, Lee SH, Yang J, et al. “Rapid and reliable computational markers of decision-making for predicting daily smoking behavior and smoking cessation treatment outcomes.” *Neuropsychopharmacology* 51, 1881–1890 (2026). [DOI](https://doi.org/10.1038/s41386-026-02448-5).

**Directly verified from the paper record:** Seventy-nine people in a 5–6-week smoking-cessation program completed daily measures of smoking, craving, stress, mood, anxiety, medication adherence, and decision-making tasks. Participants contributed an average of 23.3 daily observations. The authors evaluated time-lagged models for **next-day cigarette consumption**. [Article](https://www.nature.com/articles/s41386-026-02448-5); [PubMed](https://pubmed.ncbi.nlm.nih.gov/42215735/).

**Reported results:** The most comprehensive model under standard cross-validation had test \(R^2=0.552\). In the authors’ forward-chaining analysis, a model using prior use and craving had \(R^2=0.483\); additional EMA variables did not uniformly improve that result. These metrics concern cigarette count in that cohort and should not be compared directly with NumiKun’s daily-score \(R^2\). [Article results](https://www.nature.com/articles/s41386-026-02448-5).

**Why it matters:** A project framed as “use daily craving, mood, stress, and anxiety to predict next-day nicotine-related behavior” already has a close precedent. The paper is also valuable because it distinguishes lagged predictors from the separate question of whether evaluation itself is strictly forward in time.

**Availability:** The paper links its [analysis code and data](https://github.com/CCS-Lab/SmokingPred_ADO). I did not independently execute them or verify every file’s license.

### 6.3 EMASENS: group, individual, and hybrid prediction

**Citation:** Perski O, et al. “Supervised machine learning to predict smoking lapses from Ecological Momentary Assessments and sensor data: Implications for just-in-time adaptive intervention development.” *PLOS Digital Health* (2024). [DOI](https://doi.org/10.1371/journal.pdig.0000594).

The study used real-world EMA and wearable data during a 10-day quit attempt. Participants were prompted up to 16 times per day. Of 46 participants, 38 met the EMA adherence threshold; 30 also met the sensor-data threshold. Variables included affect, craving, quit confidence, motivation, context, caffeine, and nicotine use. [Paper](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000594).

**Reported results:** Without sensors, the best group algorithm’s pooled AUC was 0.899, while the median AUC across out-of-sample individuals was 0.639. Individual-level models could be constructed for 15 of 38 participants. With sensors, the corresponding pooled AUC was 0.952 and the median out-of-sample individual AUC was 0.745. These are different evaluation summaries; the pooled result does not guarantee strong performance for each person. [Study results](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000594).

**Availability:** [Zenodo archive](https://zenodo.org/records/12532026), [GitHub](https://github.com/OlgaPerski/EMASENS_ML), and [OSF protocol](https://osf.io/ywqpv).

**Limit:** The outcome is a momentary smoking lapse, not a daily pouch-craving score. Before implementing a prospective task, inspect the paper’s precise timing and feature definitions rather than assuming every variable was available before the event.

### 6.4 Leppin et al. (2026): burden, feature selection, and personalization

**Citation:** Leppin C, et al. “Optimising supervised machine learning algorithms predicting cigarette cravings and lapses for a smoking cessation just-in-time adaptive intervention (JITAI).” *PLOS One* (2026). [DOI](https://doi.org/10.1371/journal.pone.0349028).

This paper reuses EMASENS data from 37 participants and examines 5,964 EMA responses. It varies prompt frequency, feature count, and the proportion of a participant’s own data included in training. Across the studied configurations, the authors report median ROC-AUCs of 0.659 for lapse and 0.628 for craving. Feature reduction had little effect on lapse performance but slightly reduced craving performance; personalization effects depended on outcome and metric. [Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0349028).

**Relevance:** Feature-group comparisons, burden/performance trade-offs, and hybrid training are already established research directions. A project can apply them to a different task, but should describe that as an **application or evaluation**, unless a narrower novelty claim is substantiated.

### 6.5 Anxiety and craving: McKinty et al. (2026)

**Citation:** McKinty AA, Hatz LE, Liu W, Andrade G, Doran N, and Courtney KE. “The relationship between nicotine craving and state anxiety in daily and non-daily nicotine users.” *Addictive Behaviors* 172:108501 (2026). [DOI](https://doi.org/10.1016/j.addbeh.2025.108501).

In a laboratory VR cue-exposure study, 80 daily and 34 non-daily nicotine/tobacco users completed state-anxiety and craving assessments. The authors report that state anxiety was positively associated with pre-cue craving, while the relationship with post-cue craving differed by use group. [Article](https://www.sciencedirect.com/science/article/pii/S030646032500262X).

**Interpretation:** This supports studying anxiety and craving together, but it is an **association study in a laboratory setting**. It does not establish that a daily anxiety column predicts next-day craving, nor that the relationship is causal. The publisher states that data are available on request.

### 6.6 Within-person dynamics: Spillane and Soyster (2023)

**Citation:** Spillane JA and Soyster P. “Modeling Idiographic Longitudinal Relationships between Affect and Cigarette Use: An Ecological Momentary Assessment Study.” *Substance Use & Misuse* 58(14), 1883–1894 (2023). [DOI](https://doi.org/10.1080/10826084.2023.2257312).

Fifty-two participants completed smartphone EMA surveys four times per day for 30 days, rating discrete emotions, stress, craving, and smoking behavior. The authors used individual-level generalized linear models and reported substantial variation in the strength and direction of associations across participants. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37735802/).

**Relevance:** This is a strong reason to inspect participant-level patterns rather than rely only on a pooled association. It is not, from the information reviewed, evidence that a deployed predictive model will generalize to unseen people.

### 6.7 Sleep and craving: Freeman and Gottfredson (2018)

**Citation:** Freeman LK and Gottfredson NC. “Using ecological momentary assessment to assess the temporal relationship between sleep quality and cravings in individuals recovering from substance use disorders.” *Addictive Behaviors* 83, 95–101 (2018). [DOI](https://doi.org/10.1016/j.addbeh.2017.11.001).

The study sent 122 treatment participants four surveys per day for three weeks and examined within- and between-person relationships between sleep quality and craving. The authors reported associations in both temporal directions, with a stronger between-person component in their analysis. [PubMed](https://pubmed.ncbi.nlm.nih.gov/29137841/).

**Relevance and limit:** It motivates distinguishing a person’s usual sleep from a day that is unusually poor for that person. Its population and craving outcome should not be assumed to match nicotine-pouch users or the Kaggle score. It is not an external ML benchmark.

### 6.8 Product-specific context: oral nicotine pouches

A [randomized crossover clinical study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9217727/) compared nicotine delivery from tobacco-free oral pouches and cigarettes. It illustrates why pouch strength, nicotine delivery, and product timing cannot be assumed equivalent to cigarettes.

This is **contextual mechanism evidence**, not an EMA prediction dataset or proof about the Kaggle records. Product formulation and study conditions matter, and the paper’s funding and competing-interest statements should be examined when using it in a final literature review.

---

## 7. Cross-cutting methodological findings

| Issue | What the sources establish | Implication for this project |
|---|---|---|
| **Outcome definition** | EMASENS predicts high craving or lapse; Lee predicts next-day cigarette count; NumiKun models daily scores. | Specify the exact target and unit. Do not call a craving score a lapse or relapse. |
| **Prediction time** | Lee explicitly uses day-\(t\) variables for day-\(t+1\) smoking; NumiKun retains same-record predictors. | Build a feature-availability table for the intended cutoff. A column name alone does not establish when it was known. |
| **Temporal evaluation** | Lee compares standard and forward-chaining analyses; NumiKun’s participant-first sorting does not establish a global forward split. | Define chronological splits that match the chosen deployment setting. |
| **Participant overlap** | EMASENS evaluates group, individual, and hybrid settings separately. | Participant overlap is valid for forecasting known people if earlier information is available; it cannot demonstrate performance on unseen people. |
| **Baselines** | NumiKun reports a persistence baseline; Lee compares models with different predictor groups. | Compare against a simple baseline appropriate to the target, such as the previous observed score or training-set mean. |
| **Class imbalance** | The Smoke Free dataset reports 7.6% lapse entries. | For classification, report prevalence and precision–recall performance alongside ROC-AUC; select thresholds without using the final test set. |
| **Missing data** | EMA designs can miss surveys, and different studies apply adherence thresholds. | Document missingness by participant and day; fit imputation on training data only. The Kaggle missingness pattern remains unverified. |
| **Feature selection** | Leppin et al. evaluated reduced predictors and found effects depended on target. | Treat ablation as an empirical question; perform selection inside training folds. |
| **Interpretation** | Spillane and Soyster report individual heterogeneity; McKinty reports anxiety–craving associations. | Model importance and association do not by themselves establish causation or clinical actionability. |
| **Leakage** | Kapoor and Narayanan document leakage across ML research; the healthcare framework emphasizes prediction-time context. | Audit target construction, duplicate participants, chronological order, preprocessing, and availability of contemporaneous fields. |

The last column is **my methodological assessment** of how the sources apply; it is not a claim that every cited study made the same recommendation. [Leakage review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/); [healthcare label-leakage framework](https://pubmed.ncbi.nlm.nih.gov/37669138/).

### Synthetic-data branch

If the Kaggle publisher confirms that the data are synthetic, the project could still compare ML procedures on that file. However, a successful internal split would primarily show performance under that synthetic distribution. Claims about real users would require comparison with suitable real-world data and attention to fidelity, downstream utility, and privacy—not merely high predictive accuracy. [Synthetic patient-data study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12059695/).

If provenance remains unknown, report that uncertainty explicitly rather than categorizing the data as either synthetic or clinical.

---

## 8. Preliminary research-positioning map

The project has **not yet adopted a target or design**. The following options are research questions to evaluate after inspecting the data.

| Potential direction | Established antecedents | What could be investigated | What must be checked before claiming a contribution |
|---|---|---|---|
| **Next-day craving or anxiety regression** | NumiKun models daily scores with same-record features; Lee forecasts next-day cigarette count. | Whether past-only variables improve over persistence for a clearly defined daily target. | Exact score formula, timestamps, dataset identity, and whether similar next-day target studies already exist. |
| **Known versus unseen participants** | EMASENS and the app study compare group, individual, and hybrid approaches. | How performance changes between future records of known IDs and entirely held-out IDs. | Participant IDs must have meaningful provenance; verify whether synthetic generation makes these splits artificially easy. |
| **History plus contextual feature groups** | Lee compares predictor sets; Leppin evaluates feature reduction and burden. | Incremental value of sleep, mood, or behavior beyond prior outcomes. | Confirm availability at cutoff; avoid score components and fit selection inside training folds. This general idea is not novel. |
| **Short-history personalization** | EMASENS and Leppin examine participant-specific training data. | Whether a small initial history improves predictions for later records. | Define warm-up length and comparison population; ensure test outcomes are not used prematurely. Prior personalization methods need full review. |
| **Robustness to data provenance** | Synthetic-health literature studies fidelity and utility. | If synthetic status is confirmed, test whether observed performance is driven by generated regularities. | Obtain generation documentation and, for real-world generalization claims, a suitable independent real dataset and comparable measures. |
| **Same-day estimation versus true forecasting** | NumiKun’s candidate pipeline uses same-record features; Lee provides an explicitly lagged comparison. | Quantify how reported performance changes when predictor availability is restricted. | Verify dataset match, recreate the baseline, and establish score construction. Results should be described as an evaluation of task definitions, not proof of misconduct or universal leakage. |

### Claims to avoid

- “This is the first model to use craving, anxiety, and stress for nicotine prediction.”
- “A random row split demonstrates generalization to new participants.”
- “A high test \(R^2\) proves clinical forecasting ability.”
- “The Kaggle data were generated from Fisher, EMASENS, or another real cohort.”
- “Nicotine pouches and cigarettes are interchangeable observations.”
- “A feature’s importance shows that changing it will cause craving to change.”
- “The dataset is synthetic” or “the dataset is clinical” without provenance evidence.

A defensible eventual claim may be that the project **evaluates a particular task and validation protocol on a verified dataset version**. Whether that is novel requires an exact comparison with prior work.

---

## 9. Prioritized reading list

### Read first

1. **[Lee et al. (2026)](https://doi.org/10.1038/s41386-026-02448-5)** — closest verified daily prediction precedent; inspect the forward-chaining procedure and [repository](https://github.com/CCS-Lab/SmokingPred_ADO).
2. **[NumiKun notebook](https://raw.githubusercontent.com/NumiKun/Smoking-Addiction/main/Model/time_series_forecasting.ipynb)** — closest candidate dataset analysis; first verify the CSV match and reproduce the feature construction.
3. **[Perski et al. (2024)](https://doi.org/10.1371/journal.pdig.0000594)** — group versus person-level evaluation and feasibility of personalization.
4. **[Leppin et al. (2026)](https://doi.org/10.1371/journal.pone.0349028)** — feature reduction, measurement frequency, and personalized training on the same EMASENS cohort.
5. **[Kapoor and Narayanan](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/)** — leakage taxonomy for auditing the project’s pipeline.

### Read next, depending on the selected task

6. **[Hébert et al. (2021)](https://doi.org/10.1016/j.drugalcdep.2020.108340)** — time-to-lapse and feature selection.
7. **[Perski et al. (2023)](https://doi.org/10.1093/ntr/ntad051)** — self-initiated reports and group versus personalized classification.
8. **[Fisher and Soyster preprint and dataset](https://openesmdata.org/datasets/0037_fisher/)** — close overlap in longitudinal variables; inspect the full methods before using it as a detailed modeling precedent.
9. **[McKinty et al. (2026)](https://doi.org/10.1016/j.addbeh.2025.108501)** — anxiety and craving background, with explicit laboratory-setting limits.
10. **[Freeman and Gottfredson (2018)](https://doi.org/10.1016/j.addbeh.2017.11.001)** — within- versus between-person sleep and craving relationships.

### Contextual, rather than central

- [Nicotine-pouch pharmacokinetic crossover study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9217727/) for product differences.
- [Sleep and smoking EMA protocol](https://doi.org/10.1371/journal.pone.0334129) for a proposed measurement design; it should not be cited as completed evidence of its hypotheses.
- [Synthetic patient-data fidelity, utility, and privacy study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12059695/) if the dataset is confirmed or suspected to be synthetic.

---

## 10. Linked bibliography and unresolved questions

### Primary research

- Chatterjee S, et al. (2016). [*mCrave: Continuous Estimation of Craving During Smoking Cessation*](https://doi.org/10.1145/2971648.2971672). UbiComp conference paper.
- Freeman LK and Gottfredson NC (2018). [*Using ecological momentary assessment to assess the temporal relationship between sleep quality and cravings in individuals recovering from substance use disorders*](https://doi.org/10.1016/j.addbeh.2017.11.001).
- Hébert ET, et al. (2021). [*Predicting the first smoking lapse during a quit attempt: A machine learning approach*](https://doi.org/10.1016/j.drugalcdep.2020.108340).
- Lee J-H, et al. (2026). [*Rapid and reliable computational markers of decision-making for predicting daily smoking behavior and smoking cessation treatment outcomes*](https://doi.org/10.1038/s41386-026-02448-5).
- Leppin C, et al. (2026). [*Optimising supervised machine learning algorithms predicting cigarette cravings and lapses for a smoking cessation JITAI*](https://doi.org/10.1371/journal.pone.0349028).
- McKinty AA, et al. (2026). [*The relationship between nicotine craving and state anxiety in daily and non-daily nicotine users*](https://doi.org/10.1016/j.addbeh.2025.108501).
- Perski O, et al. (2023). [*Classification of Lapses in Smokers Attempting to Stop*](https://doi.org/10.1093/ntr/ntad051).
- Perski O, et al. (2024). [*Supervised machine learning to predict smoking lapses from Ecological Momentary Assessments and sensor data*](https://doi.org/10.1371/journal.pdig.0000594).
- Reed BW, Doran N, and Courtney KE (2023). [*Associations between nicotine product use and craving among stable daily and non-daily users*](https://doi.org/10.1016/j.addbeh.2023.107803).
- Spillane JA and Soyster P (2023). [*Modeling Idiographic Longitudinal Relationships between Affect and Cigarette Use*](https://doi.org/10.1080/10826084.2023.2257312).

### Datasets and repositories

- [Requested Kaggle dataset](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data).
- [NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction) — exact Kaggle identity unverified.
- [EMASENS repository](https://github.com/OlgaPerski/EMASENS_ML) and [archived release](https://zenodo.org/records/12532026).
- [Fisher and Soyster dataset on openESM](https://openesmdata.org/datasets/0037_fisher/).
- [Lee et al. analysis data and code](https://github.com/CCS-Lab/SmokingPred_ADO).
- [Smoke Free app data/code record](https://datacompass.lshtm.ac.uk/id/eprint/3694/).

### Methodological references

- [*Leakage and the reproducibility crisis in machine-learning-based science*](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/).
- [*A framework for understanding label leakage in machine learning for health care*](https://pubmed.ncbi.nlm.nih.gov/37669138/).
- [*On the fidelity versus privacy and utility trade-off of synthetic patient data*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12059695/).

### Unresolved questions with the greatest impact

1. What is the Kaggle file’s **actual provenance**: observed, synthetic, simulated, or unknown?
2. Does the NumiKun CSV match the Kaggle version by **hash or records**?
3. How are `Overall_Craving_Score` and `Daily_Anxiety_Score` defined, and are other columns their ingredients?
4. When is each field available relative to a prospective prediction cutoff?
5. Do participant IDs and study days represent real longitudinal observations or generated structure?
6. What license applies to the exact dataset version?
7. Which target and generalization setting does the project ultimately want to answer?

Those answers should determine which taxonomy categories become central to Milestone 2 and which remain background.

> ```yaml
> Using the sources identified in the research just completed, create a new folder at:
>
> work/andres/related_work_sources/  in (D:\GitHub\ML NJIT\MiniProject\DS675 - Smoking Addiction Dataset\work\andres )  this folder is sincrhonized with github repository via Github desktop.
>
> Repository:
> https://github.com/Andres-ArangoMartinez/DS675---Smoking-Addiction-Dataset
>
> Organize the findings in the new folder’s README.md under three sections:
>
> 1. Work using our exact dataset: repositories, notebooks, and scientific literature.
> 2. Similar datasets: datasets with related variables, populations, or predictive tasks.
> 3. Related literature: studies relevant to nicotine use, craving, anxiety, stress, sleep, and predictive modeling.
>
> For each section, create a summary table with these columns:
>
> | Work / Dataset and Authors | Brief Description: Methods and Results | Research Objective |
>
> In the first column, include the title, authors or organization, publication year when available, and a clickable link to the original source. Add associated code or dataset links when available.
>
> Keep descriptions concise and evidence-based. Clearly distinguish work using our exact dataset from work using related data. Identify proposed methods versus completed analyses, and mark information that still requires verification. Do not invent missing details or count papers using the same cohort as separate datasets.
>
> Add a short introduction explaining that this folder is a collection of sources for subsequent review and deeper development of our project’s background and related work. Include the research date.
>
> Preserve existing repository content. The deliverable should be a clear, navigable reference collection that we can expand as we review the sources.
> ```

<details><summary>6 previous messages</summary>

> I’ll check the repository’s local guidance, then create `work/andres/related_work_sources/README.md` with the three source tables and verification notes.
>
> <details><summary>Ran 7 commands</summary>
>
> - Ran `$paths = @('D:\AGENTS.md','D:\GitHub\AGENTS.md','D:\GitHub\ML NJIT\AGENTS.md','D:\GitHub\ML NJIT\MiniProject\AGENTS.md','D:\GitHub\ML NJIT\MiniProject\DS675 - Smoking Addiction Dataset\AGENTS.md'); foreach ($p in $paths) { if (Test-Path -LiteralPath $p) { Write-Output "FILE: $p"; Get-Content -LiteralPath $p } }`
> - Ran `rg -n --no-heading "DS675_MiniProject|Smoking Addiction|related.work|commit" 'C:\Users\Andres\.codex\memories\MEMORY.md'`
> - Ran `Get-Item -LiteralPath 'D:\GitHub\ML NJIT\MiniProject\DS675 - Smoking Addiction Dataset' | Select-Object FullName; Get-ChildItem -LiteralPath 'D:\GitHub\ML NJIT\MiniProject\DS675 - Smoking Addiction Dataset' -Force | Select-Object Mode,Name; git status --short; git remote -v`
> - Ran `rg --files -g AGENTS.md -g README.md -g '*Nicotine*' -g '*.csv' -g '*metadata*' -g '*related*'; Get-ChildItem -LiteralPath 'work\andres' -Force | Format-Table Mode,Name -AutoSize; Get-Content -LiteralPath '.git\config'`
> - Ran `$candidates = @('C:\Program Files\Git\cmd\git.exe','C:\Program Files\Git\bin\git.exe'); foreach ($p in $candidates) { if (Test-Path -LiteralPath $p) { Write-Output $p } }; Get-ChildItem -LiteralPath 'C:\Users\Andres\AppData\Local\GitHubDesktop' -Filter git.exe -Recurse -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName; $lines=Get-Content -LiteralPath 'C:\Users\Andres\.codex\memories\MEMORY.md'; for($i=236;$i -lt 244;$i++){ '{0}:{1}' -f ($i+1),$lines[$i] }`
> - Ran `Get-Content -LiteralPath 'README.md' -Raw; Get-Content -LiteralPath 'work\README.md' -Raw; Get-Content -LiteralPath 'data\README.md' -Raw; & 'C:\Users\Andres\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe' status --short; rg --files --hidden -g AGENTS.md -g '!\.git\**'`
> - Ran `Get-Content -LiteralPath 'CONTRIBUTING.md' -Raw; Get-Content -LiteralPath 'docs\methodology.md' -Raw; Get-Content -LiteralPath '.gitignore' -Raw`
>
> </details>
>
> The repository already describes the data as synthetic based on Kate’s proposal, while its data audit is still pending. I’ll preserve that distinction and mark the NumiKun dataset match as unverified. I’ll also link this collection to the existing project guidance and identify papers that reuse the EMASENS cohort.
>
> <details><summary>Created a file, edited a file, ran a command, searched the web</summary>
>
> - Wrote `./ML NJIT/MiniProject/DS675 - Smoking Addiction Dataset/work/andres/related_work_sources/README.md` (+65 -0)
>
> Searched the web for `https://pubmed.ncbi.nlm.nih.gov/37669138/`
>
> - Ran `& 'C:\Users\Andres\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe' status --short; & 'C:\Users\Andres\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe' diff --check; Get-Item -LiteralPath 'work\andres\related_work_sources\README.md' | Format-List FullName,Length; Get-Command python,py -ErrorAction SilentlyContinue | Select-Object Name,Source | Format-Table -AutoSize`
>
> Searched the web for `"On the fidelity versus privacy and utility trade-off of synthetic patient data" authors ...`
>
> - Wrote `./ML NJIT/MiniProject/DS675 - Smoking Addiction Dataset/work/andres/related_work_sources/README.md` (+5 -5)
>
> </details>
>
> The README now contains the three tables, source links, and notes distinguishing completed analyses, proposed work, and unresolved evidence. I’m checking the Markdown and local links, and confirming that only the new folder appears in Git’s changes.
>
> <details><summary>Ran a command</summary>
>
> - Ran `$readmePath = Join-Path (Get-Location) 'work\andres\related_work_sources\README.md'; $body = Get-Content -LiteralPath $readmePath -Raw -Encoding UTF8; $lines = Get-Content -LiteralPath $readmePath -Encoding UTF8; $headings = @($lines | Where-Object { $_ -match '^## ' }); if ($headings.Count -ne 3) { throw 'Expected exactly three main sections.' }; $headers = @($lines | Where-Object { $_ -eq '| Work / Dataset and Authors | Brief Description: Methods and Results | Research Objective |' }); if ($headers.Count -ne 3) { throw 'Expected three requested table headers.' }; $rows = @($lines | Where-Object { $_ -match '^\|' }); foreach ($row in $rows) { if (([regex]::Matches($row,'\|')).Count -ne 4) { throw "Malformed table row: $row" } }; $links = [regex]::Matches($body,'\]\(([^)]+)\)'); $localCount = 0; foreach ($match in $links) { $target = $match.Groups[1].Value; if ($target -notmatch '^https?://' -and $target -notmatch '^#') { $localCount++; $relative = ($target -split '#',2)[0]; $resolved = Join-Path (Split-Path -Parent $readmePath) $relative; if (-not (Test-Path -LiteralPath $resolved)) { throw "Broken local link: $target" } } }; if ($body.Contains([char]0xFFFD)) { throw 'Invalid replacement character found.' }; Write-Output ('Verified: {0} sections; {1} table rows including headers; {2} valid local links.' -f $headings.Count,$rows.Count,$localCount); & 'C:\Users\Andres\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe' diff --no-index --check -- /dev/null 'work/andres/related_work_sources/README.md'; if ($LASTEXITCODE -gt 1) { throw 'Git whitespace check failed.' }; & 'C:\Users\Andres\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe' status --short; & 'C:\Users\Andres\AppData\Local\GitHubDesktop\app-3.6.7\resources\app\git\cmd\git.exe' ls-files --others --exclude-standard -- 'work/andres/related_work_sources';`
>
> </details>
</details>

Created [related_work_sources/README.md](</D:/GitHub/ML NJIT/MiniProject/DS675 - Smoking Addiction Dataset/work/andres/related_work_sources/README.md>) with the three requested tables, research dates, source links, verification notes, and shared-cohort labels.

Checked table formatting and local links. Existing content is preserved. The new file is uncommitted and ready for review in GitHub Desktop.
