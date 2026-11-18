# Dataset audit — AI-assisted reproduction

The original [dataset_description.md](../../dataset_description.md) is preserved. Results below are computed from the common raw CSV.

Reference claims: **299/299 passed**; **0 failed**.

CSV SHA-256: `7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907`.

## Structure and missingness

| metric | value |
| --- | --- |
| rows | 30000 |
| columns | 35 |
| participants | 1000 |
| distinct_days | 30 |
| day_min | 1 |
| day_max | 30 |
| rows_per_person_min | 30 |
| rows_per_person_max | 30 |
| rows_per_day_min | 1000 |
| rows_per_day_max | 1000 |
| duplicate_keys_excess | 0 |
| rows_in_duplicate_keys | 0 |
| duplicate_rows_excess | 0 |
| missing_key_cells | 0 |
| participants_with_profile_changes | 0 |
| participants_without_exact_days_1_to_30 | 0 |
| balanced_keys_days_1_to_30 | True |

| column | missing | observed | percent_rows |
| --- | --- | --- | --- |
| Participant_ID | 0 | 30000 | 0.000000 |
| Day_Number | 0 | 30000 | 0.000000 |
| Age_Group | 0 | 30000 | 0.000000 |
| Gender | 0 | 30000 | 0.000000 |
| Occupation_Status | 0 | 30000 | 0.000000 |
| Nicotine_Use_Duration_Months | 0 | 30000 | 0.000000 |
| Pouches_Per_Day | 0 | 30000 | 0.000000 |
| Pouch_Strength_mg | 0 | 30000 | 0.000000 |
| First_Pouch_Time | 0 | 30000 | 0.000000 |
| Time_Since_Last_Pouch_Minutes | 355 | 29645 | 1.183333 |
| Longest_Nicotine_Free_Period_Hours | 380 | 29620 | 1.266667 |
| Morning_Cravings_Score | 369 | 29631 | 1.230000 |
| Afternoon_Cravings_Score | 373 | 29627 | 1.243333 |
| Evening_Cravings_Score | 346 | 29654 | 1.153333 |
| Overall_Craving_Score | 349 | 29651 | 1.163333 |
| Craving_Triggers | 323 | 29677 | 1.076667 |
| Craving_Intensity_Peak | 0 | 30000 | 0.000000 |
| Craving_Duration_Minutes | 0 | 30000 | 0.000000 |
| Attempted_To_Resist_Craving | 345 | 29655 | 1.150000 |
| Successfully_Resisted | 357 | 29643 | 1.190000 |
| Daily_Anxiety_Score | 0 | 30000 | 0.000000 |
| Morning_Anxiety_Score | 0 | 30000 | 0.000000 |
| Evening_Anxiety_Score | 347 | 29653 | 1.156667 |
| Perceived_Stress_Score | 0 | 30000 | 0.000000 |
| Mood_Score | 342 | 29658 | 1.140000 |
| Irritability_Score | 0 | 30000 | 0.000000 |
| Restlessness_Score | 0 | 30000 | 0.000000 |
| Sleep_Duration_Hours | 0 | 30000 | 0.000000 |
| Sleep_Quality_Score | 0 | 30000 | 0.000000 |
| Caffeine_Intake_mg | 0 | 30000 | 0.000000 |
| Exercise_Minutes | 370 | 29630 | 1.233333 |
| Screen_Time_Hours | 373 | 29627 | 1.243333 |
| Work_Or_Study_Hours | 0 | 30000 | 0.000000 |
| Major_Stress_Event_Today | 0 | 30000 | 0.000000 |
| Social_Interaction_Hours | 353 | 29647 | 1.176667 |

## Numeric measurements

| column | observed | missing | min | max | mean | median | sample_variance | sample_std | q1 | q3 | iqr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Day_Number | 30000 | 0 | 1.000000 | 30.000000 | 15.500000 | 15.500000 | 74.919164 | 8.655586 | 8.000000 | 23.000000 | 15.000000 |
| Nicotine_Use_Duration_Months | 30000 | 0 | 3.000000 | 120.000000 | 21.592000 | 16.000000 | 330.716560 | 18.185614 | 9.000000 | 29.000000 | 20.000000 |
| Pouches_Per_Day | 30000 | 0 | 0.000000 | 24.000000 | 7.430900 | 7.000000 | 18.813786 | 4.337486 | 4.000000 | 10.000000 | 6.000000 |
| Pouch_Strength_mg | 30000 | 0 | 4.000000 | 15.000000 | 7.859367 | 8.000000 | 7.288032 | 2.699636 | 6.000000 | 10.000000 | 4.000000 |
| Time_Since_Last_Pouch_Minutes | 29645 | 355 | 5.000000 | 716.000000 | 73.512768 | 43.000000 | 9212.610593 | 95.982345 | 11.000000 | 95.000000 | 84.000000 |
| Longest_Nicotine_Free_Period_Hours | 29620 | 380 | 1.000000 | 23.900000 | 6.202465 | 6.000000 | 10.002090 | 3.162608 | 4.000000 | 8.100000 | 4.100000 |
| Morning_Cravings_Score | 29631 | 369 | 0.000000 | 10.000000 | 5.542611 | 5.500000 | 2.563615 | 1.601129 | 4.500000 | 6.600000 | 2.100000 |
| Afternoon_Cravings_Score | 29627 | 373 | 0.000000 | 10.000000 | 6.333122 | 6.300000 | 2.942641 | 1.715413 | 5.200000 | 7.500000 | 2.300000 |
| Evening_Cravings_Score | 29654 | 346 | 0.400000 | 10.000000 | 5.806886 | 5.800000 | 2.579464 | 1.606071 | 4.700000 | 6.900000 | 2.200000 |
| Overall_Craving_Score | 29651 | 349 | 0.000000 | 10.000000 | 5.994904 | 6.000000 | 2.837220 | 1.684405 | 4.800000 | 7.200000 | 2.400000 |
| Craving_Intensity_Peak | 30000 | 0 | 0.000000 | 10.000000 | 6.336453 | 6.300000 | 3.048163 | 1.745899 | 5.100000 | 7.600000 | 2.500000 |
| Craving_Duration_Minutes | 30000 | 0 | 3.000000 | 180.000000 | 62.098700 | 60.000000 | 406.673714 | 20.166153 | 48.000000 | 73.000000 | 25.000000 |
| Daily_Anxiety_Score | 30000 | 0 | 0.000000 | 10.000000 | 5.311870 | 5.300000 | 3.940572 | 1.985087 | 3.900000 | 6.700000 | 2.800000 |
| Morning_Anxiety_Score | 30000 | 0 | 0.000000 | 10.000000 | 5.079220 | 5.100000 | 3.685689 | 1.919815 | 3.700000 | 6.400000 | 2.700000 |
| Evening_Anxiety_Score | 29653 | 347 | 0.000000 | 10.000000 | 5.353789 | 5.300000 | 3.894422 | 1.973429 | 4.000000 | 6.700000 | 2.700000 |
| Perceived_Stress_Score | 30000 | 0 | 0.000000 | 10.000000 | 3.119447 | 2.700000 | 4.747845 | 2.178955 | 1.500000 | 4.300000 | 2.800000 |
| Mood_Score | 29658 | 342 | 0.000000 | 10.000000 | 5.684807 | 5.700000 | 2.746568 | 1.657277 | 4.600000 | 6.900000 | 2.300000 |
| Irritability_Score | 30000 | 0 | 1.000000 | 9.300000 | 4.735713 | 4.700000 | 1.155598 | 1.074988 | 4.000000 | 5.400000 | 1.400000 |
| Restlessness_Score | 30000 | 0 | 1.400000 | 9.000000 | 5.058637 | 5.000000 | 1.004082 | 1.002039 | 4.400000 | 5.700000 | 1.300000 |
| Sleep_Duration_Hours | 30000 | 0 | 3.500000 | 11.000000 | 7.002840 | 7.000000 | 1.423813 | 1.193236 | 6.200000 | 7.800000 | 1.600000 |
| Sleep_Quality_Score | 30000 | 0 | 3.000000 | 10.000000 | 6.919580 | 6.900000 | 1.065315 | 1.032141 | 6.200000 | 7.600000 | 1.400000 |
| Caffeine_Intake_mg | 30000 | 0 | 0.000000 | 600.000000 | 160.494667 | 140.000000 | 13904.832133 | 117.918752 | 70.000000 | 220.000000 | 150.000000 |
| Exercise_Minutes | 29630 | 370 | 0.000000 | 180.000000 | 30.047114 | 25.000000 | 449.409370 | 21.199278 | 15.000000 | 41.000000 | 26.000000 |
| Screen_Time_Hours | 29627 | 373 | 1.000000 | 14.000000 | 4.025376 | 3.400000 | 7.425324 | 2.724945 | 1.900000 | 5.400000 | 3.500000 |
| Work_Or_Study_Hours | 30000 | 0 | 0.000000 | 18.000000 | 7.101423 | 7.300000 | 11.312569 | 3.363416 | 4.700000 | 9.500000 | 4.800000 |
| Social_Interaction_Hours | 29647 | 353 | 0.000000 | 10.000000 | 2.249985 | 1.800000 | 3.218762 | 1.794091 | 0.900000 | 3.100000 | 2.200000 |

Each column uses its own observed values. Standard deviation and variance use ddof=1; quartiles use linear interpolation.

## Categorical frequencies

| variable | category | unit | count | observed_denominator | total_denominator | percent_observed | percent_total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Age_Group | 18-24 | participant | 239 | 1000 | 1000 | 23.900000 | 23.900000 |
| Age_Group | 25-34 | participant | 353 | 1000 | 1000 | 35.300000 | 35.300000 |
| Age_Group | 35-44 | participant | 203 | 1000 | 1000 | 20.300000 | 20.300000 |
| Age_Group | 45-54 | participant | 122 | 1000 | 1000 | 12.200000 | 12.200000 |
| Age_Group | 55+ | participant | 83 | 1000 | 1000 | 8.300000 | 8.300000 |
| Gender | Female | participant | 482 | 1000 | 1000 | 48.200000 | 48.200000 |
| Gender | Male | participant | 453 | 1000 | 1000 | 45.300000 | 45.300000 |
| Gender | Non-binary | participant | 41 | 1000 | 1000 | 4.100000 | 4.100000 |
| Gender | Prefer_not_to_say | participant | 24 | 1000 | 1000 | 2.400000 | 2.400000 |
| Occupation_Status | Employed | participant | 488 | 1000 | 1000 | 48.800000 | 48.800000 |
| Occupation_Status | Homemaker | participant | 63 | 1000 | 1000 | 6.300000 | 6.300000 |
| Occupation_Status | Retired | participant | 82 | 1000 | 1000 | 8.200000 | 8.200000 |
| Occupation_Status | Self_Employed | participant | 123 | 1000 | 1000 | 12.300000 | 12.300000 |
| Occupation_Status | Student | participant | 156 | 1000 | 1000 | 15.600000 | 15.600000 |
| Occupation_Status | Unemployed | participant | 88 | 1000 | 1000 | 8.800000 | 8.800000 |
| Craving_Triggers | After_Meal | participant-day | 2955 | 29677 | 30000 | 9.957206 | 9.850000 |
| Craving_Triggers | Alcohol | participant-day | 607 | 29677 | 30000 | 2.045355 | 2.023333 |
| Craving_Triggers | Boredom | participant-day | 3505 | 29677 | 30000 | 11.810493 | 11.683333 |
| Craving_Triggers | Caffeine | participant-day | 1182 | 29677 | 30000 | 3.982882 | 3.940000 |
| Craving_Triggers | Habit | participant-day | 2390 | 29677 | 30000 | 8.053375 | 7.966667 |
| Craving_Triggers | Morning | participant-day | 2960 | 29677 | 30000 | 9.974054 | 9.866667 |
| Craving_Triggers | Other | participant-day | 870 | 29677 | 30000 | 2.931563 | 2.900000 |
| Craving_Triggers | Social_Situation | participant-day | 2413 | 29677 | 30000 | 8.130876 | 8.043333 |
| Craving_Triggers | Stress | participant-day | 6077 | 29677 | 30000 | 20.477137 | 20.256667 |
| Craving_Triggers | Study | participant-day | 2363 | 29677 | 30000 | 7.962395 | 7.876667 |
| Craving_Triggers | Withdrawal | participant-day | 1430 | 29677 | 30000 | 4.818546 | 4.766667 |
| Craving_Triggers | Work | participant-day | 2925 | 29677 | 30000 | 9.856118 | 9.750000 |
| First_Pouch_Time | 05:00 | participant-day | 715 | 30000 | 30000 | 2.383333 | 2.383333 |
| First_Pouch_Time | 05:15 | participant-day | 706 | 30000 | 30000 | 2.353333 | 2.353333 |
| First_Pouch_Time | 05:30 | participant-day | 665 | 30000 | 30000 | 2.216667 | 2.216667 |
| First_Pouch_Time | 05:45 | participant-day | 676 | 30000 | 30000 | 2.253333 | 2.253333 |
| First_Pouch_Time | 06:00 | participant-day | 1224 | 30000 | 30000 | 4.080000 | 4.080000 |
| First_Pouch_Time | 06:15 | participant-day | 1130 | 30000 | 30000 | 3.766667 | 3.766667 |
| First_Pouch_Time | 06:30 | participant-day | 1219 | 30000 | 30000 | 4.063333 | 4.063333 |
| First_Pouch_Time | 06:45 | participant-day | 1165 | 30000 | 30000 | 3.883333 | 3.883333 |
| First_Pouch_Time | 07:00 | participant-day | 1902 | 30000 | 30000 | 6.340000 | 6.340000 |
| First_Pouch_Time | 07:15 | participant-day | 1813 | 30000 | 30000 | 6.043333 | 6.043333 |
| First_Pouch_Time | 07:30 | participant-day | 1853 | 30000 | 30000 | 6.176667 | 6.176667 |
| First_Pouch_Time | 07:45 | participant-day | 1836 | 30000 | 30000 | 6.120000 | 6.120000 |
| First_Pouch_Time | 08:00 | participant-day | 1921 | 30000 | 30000 | 6.403333 | 6.403333 |
| First_Pouch_Time | 08:15 | participant-day | 1814 | 30000 | 30000 | 6.046667 | 6.046667 |
| First_Pouch_Time | 08:30 | participant-day | 1878 | 30000 | 30000 | 6.260000 | 6.260000 |
| First_Pouch_Time | 08:45 | participant-day | 1879 | 30000 | 30000 | 6.263333 | 6.263333 |
| First_Pouch_Time | 09:00 | participant-day | 1211 | 30000 | 30000 | 4.036667 | 4.036667 |
| First_Pouch_Time | 09:15 | participant-day | 1227 | 30000 | 30000 | 4.090000 | 4.090000 |
| First_Pouch_Time | 09:30 | participant-day | 1265 | 30000 | 30000 | 4.216667 | 4.216667 |
| First_Pouch_Time | 09:45 | participant-day | 1255 | 30000 | 30000 | 4.183333 | 4.183333 |
| First_Pouch_Time | 10:00 | participant-day | 474 | 30000 | 30000 | 1.580000 | 1.580000 |
| First_Pouch_Time | 10:15 | participant-day | 459 | 30000 | 30000 | 1.530000 | 1.530000 |
| First_Pouch_Time | 10:30 | participant-day | 519 | 30000 | 30000 | 1.730000 | 1.730000 |
| First_Pouch_Time | 10:45 | participant-day | 509 | 30000 | 30000 | 1.696667 | 1.696667 |
| First_Pouch_Time | 11:00 | participant-day | 133 | 30000 | 30000 | 0.443333 | 0.443333 |
| First_Pouch_Time | 11:15 | participant-day | 158 | 30000 | 30000 | 0.526667 | 0.526667 |
| First_Pouch_Time | 11:30 | participant-day | 136 | 30000 | 30000 | 0.453333 | 0.453333 |
| First_Pouch_Time | 11:45 | participant-day | 151 | 30000 | 30000 | 0.503333 | 0.503333 |
| First_Pouch_Time | 12:00 | participant-day | 24 | 30000 | 30000 | 0.080000 | 0.080000 |
| First_Pouch_Time | 12:15 | participant-day | 24 | 30000 | 30000 | 0.080000 | 0.080000 |
| First_Pouch_Time | 12:30 | participant-day | 20 | 30000 | 30000 | 0.066667 | 0.066667 |
| First_Pouch_Time | 12:45 | participant-day | 27 | 30000 | 30000 | 0.090000 | 0.090000 |
| First_Pouch_Time | 13:00 | participant-day | 2 | 30000 | 30000 | 0.006667 | 0.006667 |
| First_Pouch_Time | 13:15 | participant-day | 2 | 30000 | 30000 | 0.006667 | 0.006667 |
| First_Pouch_Time | 13:30 | participant-day | 2 | 30000 | 30000 | 0.006667 | 0.006667 |
| First_Pouch_Time | 13:45 | participant-day | 5 | 30000 | 30000 | 0.016667 | 0.016667 |
| First_Pouch_Time | 14:00 | participant-day | 1 | 30000 | 30000 | 0.003333 | 0.003333 |
| Attempted_To_Resist_Craving | No | participant-day | 8332 | 29655 | 30000 | 28.096442 | 27.773333 |
| Attempted_To_Resist_Craving | Yes | participant-day | 21323 | 29655 | 30000 | 71.903558 | 71.076667 |
| Successfully_Resisted | No | participant-day | 19333 | 29643 | 30000 | 65.219445 | 64.443333 |
| Successfully_Resisted | Yes | participant-day | 10310 | 29643 | 30000 | 34.780555 | 34.366667 |
| Major_Stress_Event_Today | No | participant-day | 28524 | 30000 | 30000 | 95.080000 | 95.080000 |
| Major_Stress_Event_Today | Yes | participant-day | 1476 | 30000 | 30000 | 4.920000 | 4.920000 |

Demographics count participants once after checking profile invariance. Other frequencies count participant-days. Missing cells are excluded from the observed denominator.

## Target distribution

| interval | count | percent_observed |
| --- | --- | --- |
| [0, 1) | 28 | 0.094432 |
| [1, 2) | 163 | 0.549729 |
| [2, 3) | 833 | 2.809349 |
| [3, 4) | 2405 | 8.111025 |
| [4, 5) | 4601 | 15.517183 |
| [5, 6) | 6659 | 22.457927 |
| [6, 7) | 6404 | 21.597922 |
| [7, 8) | 4614 | 15.561027 |
| [8, 9) | 2704 | 9.119423 |
| [9, 10] | 1240 | 4.181984 |

Bins are left-closed/right-open, except [9, 10], which includes 10. Percentages divide by the observed target count.

## Longitudinal description

| metric | value |
| --- | --- |
| status | computed |
| participants_with_variation | 1000 |
| observations_per_person_min | 27 |
| observations_per_person_max | 30 |
| person_mean_min | 1.490000 |
| person_mean_max | 9.836667 |
| daily_mean_min | 5.956535 |
| daily_mean_max | 6.043984 |
| potential_adjacent_pairs | 29000 |
| valid_adjacent_pairs | 28338 |
| pairs_excluded_for_missing_values | 662 |
| pooled_lag1_pearson | 0.858927 |
| person_centered_lag1_pearson | -0.035083 |
| centering_policy | Subtract each participant's mean of all observed target values before selecting complete consecutive-day pairs. |

Only actual consecutive days with both target values observed contribute to correlations. Centering uses each participant's full observed mean for description, not forecasting.

Additional conceptual extension (not an original reference claim): weighted between/within sums of squares.

| metric | value |
| --- | --- |
| total | 84123.580002 |
| within | 11485.762799 |
| between | 72637.817203 |
| decomposition_residual | -0.000000 |
| between_share | 0.863466 |
| interpretation | Descriptive weighted sum-of-squares share, not an ICC or causal fraction. |

## Syntactic and range checks

| rule | column | eligible | flagged |
| --- | --- | --- | --- |
| score_in_0_to_10 | Morning_Cravings_Score | 29631 | 0 |
| score_in_0_to_10 | Afternoon_Cravings_Score | 29627 | 0 |
| score_in_0_to_10 | Evening_Cravings_Score | 29654 | 0 |
| score_in_0_to_10 | Overall_Craving_Score | 29651 | 0 |
| score_in_0_to_10 | Daily_Anxiety_Score | 30000 | 0 |
| score_in_0_to_10 | Morning_Anxiety_Score | 30000 | 0 |
| score_in_0_to_10 | Evening_Anxiety_Score | 29653 | 0 |
| score_in_0_to_10 | Perceived_Stress_Score | 30000 | 0 |
| score_in_0_to_10 | Mood_Score | 29658 | 0 |
| score_in_0_to_10 | Irritability_Score | 30000 | 0 |
| score_in_0_to_10 | Restlessness_Score | 30000 | 0 |
| score_in_0_to_10 | Sleep_Quality_Score | 30000 | 0 |
| score_in_0_to_10 | Craving_Intensity_Peak | 30000 | 0 |
| nonnegative | Day_Number | 30000 | 0 |
| nonnegative | Nicotine_Use_Duration_Months | 30000 | 0 |
| nonnegative | Pouches_Per_Day | 30000 | 0 |
| nonnegative | Pouch_Strength_mg | 30000 | 0 |
| nonnegative | Time_Since_Last_Pouch_Minutes | 29645 | 0 |
| nonnegative | Longest_Nicotine_Free_Period_Hours | 29620 | 0 |
| nonnegative | Craving_Duration_Minutes | 30000 | 0 |
| nonnegative | Sleep_Duration_Hours | 30000 | 0 |
| nonnegative | Caffeine_Intake_mg | 30000 | 0 |
| nonnegative | Exercise_Minutes | 29630 | 0 |
| nonnegative | Screen_Time_Hours | 29627 | 0 |
| nonnegative | Work_Or_Study_Hours | 30000 | 0 |
| nonnegative | Social_Interaction_Hours | 29647 | 0 |
| HH:MM | First_Pouch_Time | 30000 | 0 |
| Yes_or_No | Attempted_To_Resist_Craving | 29655 | 0 |
| Yes_or_No | Successfully_Resisted | 29643 | 0 |
| Yes_or_No | Major_Stress_Event_Today | 30000 | 0 |

## Semantic flags

| check | count | eligible | percent_eligible |
| --- | --- | --- | --- |
| zero_pouches_with_first_time | 358 | 358 | 100.000000 |
| zero_pouches_with_time_since_last | 355 | 358 | 99.162011 |
| overall_above_peak | 7078 | 29651 | 23.871033 |
| success_without_attempt | 0 | 29299 | 0.000000 |
| missing_overall_with_complete_components | 339 | 349 | 97.134670 |

These flags require field definitions; they do not automatically establish data errors or justify reconstructing missing targets.

## Types and reproducibility

Environment: {'python': '3.14.4', 'pandas': '3.0.6', 'numpy': '2.4.4'}. Native dtypes: {'float64': 20, 'str': 9, 'int64': 6}. Audit dtypes: {'float64': 20, 'object': 9, 'int64': 6}.

The explicit object dtype for text columns reproduces the historical audit. This differs from pandas 3's default str inference without changing numeric measurements.

## Reference disagreements

No numerical disagreements at the precision published in the reference.

## Interpretation limits

CSV calculations establish structure and descriptive values. Synthetic status, instrument validity, generator rules, license, and clinical or causal validity require external documentation. Hash identity does not establish origin. Missingness percentages do not establish MCAR/MAR/MNAR. Correlations do not establish independence or predictive performance.

Full per-variable inventory, participant summaries, day summaries, pair evidence, and comparisons are provided in adjacent CSV/JSON files. See the notebook for the concepts and explicit calculation steps.
