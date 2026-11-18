# DS675 — Descripción y validación del conjunto de datos

*Documento de apoyo para la sección «Dataset Description and Learning Objective» del Milestone 4.*

## 1. Descripción del dataset

**Alcance.**  **Desarrollo de la descripción y evaluación del dataset** 

**Base de evidencia.** Los recuentos y estadísticos que siguen proceden de la inspección de los **30,000 registros completos de una copia CSV pública** del repositorio [NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction/blob/main/Dataset/Nicotine_Craving_Anxiety_Dynamics_30Days.csv), auditada a través de su contenido íntegro en GitHub. Se distingue esta evidencia de las características publicadas en la [página del dataset en Kaggle](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data). 


### Enfoque de revisión y responsabilidades analíticas

La revisión se realizó aplicando cinco perspectivas de análisis.

| Perspectiva | Pregunta que guía la revisión | Evidencia examinada |
| --- | --- | --- |
| **Auditoría de datos / ingeniería de datos** | ¿El CSV es legible, íntegro y consistente en sus claves y tipos? | Filas, columnas, duplicados, rangos, formatos y ausencias |
| **Estadística descriptiva** | ¿Cómo se distribuyen los registros y las mediciones? | Frecuencias, cuartiles, dispersión y distribución del craving |
| **Análisis longitudinal** | ¿Qué significan las mediciones repetidas y cómo varían dentro de cada participante? | Panel participante–día, constancia del perfil, variación intrapersonal y correlación temporal descriptiva |
| **Validez científica y de datos sintéticos** | ¿Qué interpretaciones son legítimas y cuáles necesitan definiciones del generador? | Coherencia semántica de campos, ausencia de instrumento clínico y límites de generalización |
| **Revisión académica de la rúbrica** | ¿La descripción ofrece datos suficientes para juzgar la idoneidad del recurso? | Fuente, usos posibles, clase de información, tamaños, tipos, integridad, limitaciones y trazabilidad |

El objetivo de estas perspectivas es **describir correctamente el recurso disponible**.

### 1.1 Identificación, procedencia y naturaleza

- **Nombre mostrado por Kaggle:** *Smoking Addiction Dataset / The Nicotine Craving and Anxiety Dynamics Dataset*.
- **Publicador indicado por la URL oficial:** cuenta `datascikhan` (DataSciKhan). [Ficha de Kaggle](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data).
- **Formato inspeccionado:** CSV tabular con cabecera, denominado `Nicotine_Craving_Anxiety_Dynamics_30Days.csv`.
- **Naturaleza:** datos **sintéticos** que simulan conductas de consumo de bolsas orales de nicotina (*nicotine pouches*), intensidad de craving (deseo de consumir), condiciones psicológicas y hábitos cotidianos. No son expedientes clínicos de 1,000 personas reales.
- **Unidad de observación:** un **participante simulado en un día**. Cada combinación `Participant_ID`–`Day_Number` identifica una observación.
- **Posibles usos académicos:** análisis exploratorio de mediciones repetidas; descripción de relaciones estadísticas entre craving, ansiedad, consumo y hábitos; ilustración de problemas de regresión o clasificación supervisada si se selecciona expresamente una variable resultado. **No hay una etiqueta de clase predefinida para todo el conjunto**, ya que contiene simultáneamente puntuaciones numéricas e indicadores categóricos.

Esta procedencia importa para interpretar cualquier análisis: aunque las columnas aluden a constructos empleados en investigación sobre uso de nicotina, no puede presumirse que las magnitudes, asociaciones o respuestas humanas reales se reproduzcan fielmente en una simulación. Los 30 días representan **índices consecutivos dentro de cada participante**; el CSV no proporciona una fecha de calendario de inicio ni marcas temporales completas de cada evaluación. `First_Pouch_Time` es una hora de la jornada (HH:MM), no un timestamp que determine por sí solo la fecha de observación.

### 1.2 Tamaño y estructura longitudinal de los registros

| Característica examinada | Resultado en el CSV |
| --- | ---: |
| Filas de datos | **30,000** |
| Columnas | **35** |
| Participantes distintos | **1,000** |
| Valores distintos de `Day_Number` | **30 (1–30)** |
| Observaciones por participante | **30 para todos** |
| Observaciones por día de la serie | **1,000 para cada día** |
| Combinaciones participante-día duplicadas | **0** |
| Filas completas duplicadas | **0** |
| Filas con un número incorrecto de campos | **0** |
| Participantes con atributos de perfil inconsistentes entre sus días | **0** (en las cuatro variables comprobadas) |

La estructura es un **panel balanceado en las claves**: aparecen los 30 días de todos los participantes. Esto **no** significa que todas las celdas estén presentes. Los registros pertenecientes a un mismo participante están relacionados entre sí; no deben describirse como 30,000 sujetos independientes. Los campos de perfil `Age_Group`, `Gender`, `Occupation_Status` y `Nicotine_Use_Duration_Months` son constantes dentro de cada participante a lo largo de los 30 días examinados.

### 1.3 Inventario y organización conceptual de las 35 columnas

La agrupación siguiente es una **clasificación analítica de los campos**, congruente con la revisión del curso; no se presenta como una ontología formal o un diccionario de datos publicado por el generador.

| Grupo temático | Columnas | Contenido representado |
| --- | ---: | --- |
| Identificación temporal y de sujetos | **2** | Clave del participante e índice del día |
| Características demográficas | **3** | Intervalo de edad, género y ocupación |
| Consumo de nicotina y craving | **15** | Antigüedad de uso, pouches, dosis, tiempos de uso, puntuaciones y resistencia |
| Estados psicológicos | **7** | Ansiedad, estrés, ánimo, irritabilidad e inquietud |
| Hábitos y actividades | **8** | Sueño, cafeína, ejercicio, pantalla, trabajo/estudio, eventos estresantes e interacción social |
| **Total** | **35** | |

**Tipos de datos observados.** La inspección de valores y celdas vacías indica: **20 columnas `float64`**, **6 `int64`** y **9 `object`**. Las columnas categóricas e indicadores binarios `Yes`/`No` se guardan como texto. `First_Pouch_Time` se almacena como cadena horaria. Algunas cantidades conceptualmente enteras (`Exercise_Minutes`, `Time_Since_Last_Pouch_Minutes`) se inferirían como `float64` cuando se cargan con `NaN`.

### 1.4 Perfil de los participantes simulados

Las siguientes frecuencias se calculan **una sola vez por `Participant_ID`** (base = 1,000), no sobre las 30 filas repetidas por participante.

| Variable | Categorías y participantes |
| --- | --- |
| `Age_Group` | 18–24: **239**; 25–34: **353**; 35–44: **203**; 45–54: **122**; 55+: **83** |
| `Gender` | Female: **482**; Male: **453**; Non-binary: **41**; Prefer_not_to_say: **24** |
| `Occupation_Status` | Employed: **488**; Student: **156**; Self_Employed: **123**; Unemployed: **88**; Retired: **82**; Homemaker: **63** |

El archivo recoge grupos de edad y no edad exacta; las categorías de género se reproducen con sus valores de archivo, sin asignarles interpretaciones adicionales. La distribución describe **el universo simulado en esta copia**, no la composición demográfica del consumo real de nicotina.

### 1.5 Características descriptivas de las mediciones

Los rangos son **mínimos y máximos observados**. Los ejemplos muestran tanto variables de intensidad como cantidades y duración.

| Campo | N observado | Mínimo–máximo | Media | Mediana |
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

Hay **12 categorías observadas** en `Craving_Triggers`; las más frecuentes son `Stress` (**6,077 registros**) y `Boredom` (**3,505**), contabilizadas entre las celdas no vacías. En `Major_Stress_Event_Today`, **1,476** registros contienen `Yes` y **28,524** contienen `No`. Esto caracteriza la codificación, sin interpretar los desencadenantes o eventos como causas demostradas de craving.

### 1.6 Variable numérica de craving y su distribución

`Overall_Craving_Score` es una puntuación numérica de craving global; es **una posible variable de resultado** que contiene el CSV. Aquí se la describe como dato disponible, **sin definir todavía una tarea de predicción**. Su fórmula de cálculo, validación psicométrica y origen de simulación no pudieron establecerse con los valores del CSV solamente.

| Indicador | Valor calculado |
| --- | ---: |
| Registros totales | 30,000 |
| Valores observados | **29,651 (98.84%)** |
| Valores ausentes | **349 (1.16%)** |
| Mínimo / máximo | **0 / 10** |
| Media | **5.994904** |
| Mediana | **6.0** |
| Desviación estándar muestral | **1.684405** |
| Cuartil inferior (Q1) / superior (Q3) | **4.8 / 7.2** |
| Variación de la puntuación entre días dentro del mismo participante | **1,000 de 1,000** participantes con más de un valor distinto observado |
| Cantidad de mediciones no faltantes de esta variable por participante | **27–30** |

**Distribución de frecuencias** (se usa un extremo superior exclusivo en cada intervalo, salvo el último, que incluye 10):

| Intervalo | Registros | Intervalo | Registros |
| --- | ---: | --- | ---: |
| [0, 1) | 28 | [5, 6) | 6,659 |
| [1, 2) | 163 | [6, 7) | 6,404 |
| [2, 3) | 833 | [7, 8) | 4,614 |
| [3, 4) | 2,405 | [8, 9) | 2,704 |
| [4, 5) | 4,601 | [9, 10] | 1,240 |

La distribución se concentra en valores intermedios: el 50% central está entre **4.8 y 7.2**. Los promedios diarios observados oscilan aproximadamente entre **5.957 y 6.044**; esa estabilidad del promedio agregado no prueba independencia temporal ni ausencia de patrones individuales. Las puntuaciones de mañana, tarde y noche son columnas del registro diario; **no** deben describirse como una secuencia EMA de alta frecuencia sin un esquema temporal de mediciones independientes que lo respalde.

### 1.6.1 Estructura temporal: variación dentro y entre participantes

Las **30 observaciones de cada sujeto** permiten distinguir dos fuentes diferentes de variabilidad. Los 1,000 participantes presentan al menos dos valores distintos de `Overall_Craving_Score` entre sus mediciones observadas, mientras que sus **medias individuales** oscilan aproximadamente entre **1.49 y 9.84**. Esta heterogeneidad entre sujetos es importante para interpretar cualquier estadística que agrupe todas las filas.

En **28,338 pares de días consecutivos** donde se observaron ambos valores de craving global, la correlación de Pearson agrupando participantes y días es aproximadamente **0.859**. Sin embargo, al restar a cada valor la media observada de su propio participante, la correlación entre desviaciones de días consecutivos es aproximadamente **−0.035**. Este contraste **no es una evaluación predictiva**: muestra que la correlación agrupada recoge en gran medida diferencias estables entre participantes y no debe confundirse con autocorrelación de las fluctuaciones dentro de cada sujeto. El segundo valor es descriptivo y depende, entre otras cosas, de cómo se centran los datos; por sí solo tampoco demuestra ausencia de información temporal ni independencia estadística.

El archivo usa un índice de días de **1 a 30**, pero carece de fechas calendario y de marcas de tiempo completas para cada evaluación diaria. No debe describirse como una serie de EMA a intervalos horarios o como 30 días compartidos de un mismo calendario poblacional.

### 1.7 Integridad, datos ausentes y consistencia

El CSV conserva la estructura longitudinal de las claves, pero contiene valores faltantes en **14 de las 35 columnas**:

- **4,982 celdas vacías** sobre 1,050,000 celdas (aproximadamente **0.47%** del total).
- **4,630 filas** con al menos una ausencia (**15.43%** de los 30,000 registros).
- **21 columnas completas** y **14 incompletas**.
- Las proporciones de faltantes por columna incompleta oscilan entre **1.08% y 1.27%**.
- La variable `Overall_Craving_Score` tiene **349 valores faltantes**, que no deben confundirse con registros inexistentes ni sustituirse automáticamente por ceros.

| Columna con ausencias | Faltantes | % de 30,000 |
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
| **Total** | **4,982** | **0.47% de todas las celdas** |

Los controles de validez sintáctica y de rangos no detectaron: **(a)** puntuaciones fuera de [0,10] en las 13 variables de tipo *score* evaluadas; **(b)** valores negativos en 13 campos seleccionados de cantidades y duraciones; **(c)** valores de `First_Pouch_Time` fuera de formato válido `HH:MM`; **(d)** categorías distintas de `Yes` o `No` en los tres indicadores binarios; ni **(e)** cambios intraparticipante en las cuatro variables de perfil estable examinadas.

Estos controles documentan **consistencia interna básica**, no verifican que las cifras sean fisiológicamente plausibles, que las ausencias sean aleatorias, que las mediciones sean independientes o que el simulador reproduzca comportamientos humanos. Tampoco hay una fórmula auditada que explique cómo se derivó `Overall_Craving_Score` a partir de otras variables.

### 1.7.1 Comprobaciones de coherencia semántica: casos que requieren definición

Además de verificar formatos y rangos, se analizaron **relaciones entre campos**. Surgieron observaciones que **no deben etiquetarse automáticamente como errores** sin disponer del diccionario de variables o del procedimiento que generó los registros:

| Comprobación entre campos | Resultado observado | Lectura correcta |
| --- | ---: | --- |
| `Pouches_Per_Day = 0`, pero `First_Pouch_Time` contiene una hora | **358 registros** | Sería llamativo si la hora significara necesariamente el primer pouch consumido *ese mismo día*; también podría representar una hora habitual o programada. Requiere definición. |
| `Pouches_Per_Day = 0`, con `Time_Since_Last_Pouch_Minutes` informado | **355 registros** | No demuestra inconsistencia si el último pouch ocurrió antes del día registrado; la semántica del intervalo es desconocida. |
| `Overall_Craving_Score` superior a `Craving_Intensity_Peak` | **7,078 registros** con objetivo observado | Bajo una interpretación literal de «pico diario» y «promedio diario» sería sorprendente; los nombres por sí solos no prueban que ambas escalas sean componentes comparables. |
| `Successfully_Resisted = Yes` y `Attempted_To_Resist_Craving = No` | **0 registros** | No se observó esta incompatibilidad aparente en los campos informados. |
| `Overall_Craving_Score` ausente y las tres puntuaciones de mañana/tarde/noche presentes | **339 registros** | La existencia de componentes observados no justifica reconstruir automáticamente el valor global, cuya fórmula no está verificada. |

Estas comprobaciones aportan **advertencias sobre definición y calidad semántica**, no pruebas de mala generación o de falsedad clínica. El CSV permite verificar valores y relaciones lógicas propuestas, pero no la intención de su autor. Es especialmente importante no asumir que las distintas puntuaciones de craving proceden de una escala clínica validada o que el `Overall_Craving_Score` sea una media algebraica de mañana, tarde y noche.

### 1.8 Idoneidad y límites como fuente de datos para un curso de aprendizaje supervisado

El conjunto es **estructuralmente apto** para un trabajo de aprendizaje supervisado porque reúne una variable numérica de resultado susceptible de ser elegida, distintos campos predictivos numéricos y categóricos, 1,000 series individuales con orden diario y un tamaño de archivo manejable. También contiene indicadores binarios que, si se definiera otra tarea, podrían ser variables objetivo; **el archivo no trae por sí mismo una única clasificación de clases para todo el dataset**.

Su idoneidad debe interpretarse con las siguientes reservas:

1. **Simulación, no cohorte clínica:** el tamaño aparente no equivale a 1,000 personas reales ni permite extrapolaciones médicas.
2. **Horizonte corto y sin fechas reales:** hay solo 30 posiciones diarias; no se documentan tendencias de calendario, estacionalidad anual ni zonas horarias.
3. **Campos parcialmente ausentes:** 349 valores de craving global faltantes y 13 columnas adicionales incompletas.
4. **Definiciones semánticas incompletas:** sin generador ni diccionario formal no pueden resolverse las alertas entre `Pouches_Per_Day`, `First_Pouch_Time`, `Overall_Craving_Score` y `Craving_Intensity_Peak`, ni descartarse relaciones mecánicas entre puntuaciones del mismo día.
5. **Dependencia y heterogeneidad entre filas:** 30 registros del mismo participante no son 30 observaciones estadísticamente independientes; la correlación agrupada no equivale a la correlación dentro del participante.
6. **Procedencia/versionado:** la copia auditada es pública, pero su equivalencia exacta con la descarga oficial seleccionada por el grupo permanece sin demostrar.

Por tanto, una descripción académica correcta debe presentar este recurso como **datos longitudinales sintéticos útiles para examinar técnicas de ML y relaciones dentro de la simulación**, no como evidencia de prevalencia, eficacia clínica o causalidad.

### 1.9 Registro de procedencia y verificabilidad

| Elemento | Estado y evidencia |
| --- | --- |
| Página de publicación | [Kaggle — DataSciKhan](https://www.kaggle.com/datasets/datascikhan/the-nicotine-craving-and-anxiety-dynamics-dataset/data) |
| Copia CSV leída y auditada | [GitHub — NumiKun/Smoking-Addiction](https://github.com/NumiKun/Smoking-Addiction/blob/main/Dataset/Nicotine_Craving_Anxiety_Dynamics_30Days.csv) |
| Archivo | `Nicotine_Craving_Anxiety_Dynamics_30Days.csv` |
| Tamaño de la copia leída | **4,286,125 bytes** |
| SHA-256 de la copia leída | `7218b9c5925d3c4b69ef7dc0153861778f8a9e4deb67dfa5a7242c7a0d13b907` |
| Identificador Git del blob | `80bbba4a3289940698a2926618bf0f5f1525e69f` |
| Auditoría de contenido | **Completada para esta copia**: estructura, tipos inferidos, faltantes, rangos, duplicados, perfiles, estadísticos y controles semánticos preliminares |
| Versión exacta y licencia del archivo en Kaggle | **No verificadas** (página disponible como referencia, descarga/metadata no recuperadas) |
| Igualdad byte a byte entre Kaggle y copia auditada | **No demostrada**; requiere el archivo original de la versión elegida |

La cadena SHA-256 identifica el contenido auditado, **no constituye prueba de que proceda de Kaggle**. Cuando se obtenga la descarga oficial, su hash puede compararse con esta cadena; si difiere, todos los resultados deberán verificarse nuevamente sobre el archivo adoptado. Asimismo, la estructura del CSV por sí sola no acredita una licencia de reutilización.

---

## Anexo A. Inventario exhaustivo de variables auditadas

Los tipos se indican como inferencia de lectura habitual de CSV en pandas; las unidades semánticas que aparecen en los nombres son orientativas y no sustituyen un diccionario de datos validado.

| Grupo | Columna | Tipo esperado | Faltantes | Rango o categorías observadas | Interpretación del campo |
| --- | --- | --- | ---: | --- | --- |
| Identificación | `Participant_ID` | `object` | 0 | 1,000 IDs | Clave del participante simulado |
| Identificación | `Day_Number` | `int64` | 0 | 1–30 | Índice de día dentro del participante |
| Demografía | `Age_Group` | `object` | 0 | 5 categorías | Edad por intervalos, no edad exacta |
| Demografía | `Gender` | `object` | 0 | 4 categorías | Género categórico |
| Demografía | `Occupation_Status` | `object` | 0 | 6 categorías | Situación ocupacional |
| Nicotina y craving | `Nicotine_Use_Duration_Months` | `int64` | 0 | 3–120 | Antigüedad declarada del consumo, en meses |
| Nicotina y craving | `Pouches_Per_Day` | `int64` | 0 | 0–24 | Número diario de bolsas de nicotina |
| Nicotina y craving | `Pouch_Strength_mg` | `int64` | 0 | 4–15 | Concentración por bolsa, en mg según el nombre |
| Nicotina y craving | `First_Pouch_Time` | `object` | 0 | 37 valores HH:MM | Hora de la primera bolsa; texto horario |
| Nicotina y craving | `Time_Since_Last_Pouch_Minutes` | `float64` | 355 | 5–716 | Minutos desde el último uso |
| Nicotina y craving | `Longest_Nicotine_Free_Period_Hours` | `float64` | 380 | 1–23.9 | Intervalo máximo sin nicotina, horas |
| Nicotina y craving | `Morning_Cravings_Score` | `float64` | 369 | 0–10 | Puntuación de craving en la mañana |
| Nicotina y craving | `Afternoon_Cravings_Score` | `float64` | 373 | 0–10 | Puntuación de craving en la tarde |
| Nicotina y craving | `Evening_Cravings_Score` | `float64` | 346 | 0.4–10 | Puntuación de craving en la noche |
| Nicotina y craving | `Overall_Craving_Score` | `float64` | 349 | 0–10 | Puntuación global de craving |
| Nicotina y craving | `Craving_Triggers` | `object` | 323 | 12 categorías | Desencadenante categórico del craving |
| Nicotina y craving | `Craving_Intensity_Peak` | `float64` | 0 | 0–10 | Puntuación de máxima intensidad |
| Nicotina y craving | `Craving_Duration_Minutes` | `int64` | 0 | 3–180 | Duración del craving, minutos |
| Nicotina y craving | `Attempted_To_Resist_Craving` | `object` | 345 | Yes / No | Indicador declarado de intento de resistencia |
| Nicotina y craving | `Successfully_Resisted` | `object` | 357 | Yes / No | Indicador declarado de resistencia exitosa |
| Psicología | `Daily_Anxiety_Score` | `float64` | 0 | 0–10 | Ansiedad diaria |
| Psicología | `Morning_Anxiety_Score` | `float64` | 0 | 0–10 | Ansiedad matutina |
| Psicología | `Evening_Anxiety_Score` | `float64` | 347 | 0–10 | Ansiedad nocturna |
| Psicología | `Perceived_Stress_Score` | `float64` | 0 | 0–10 | Estrés percibido |
| Psicología | `Mood_Score` | `float64` | 342 | 0–10 | Estado de ánimo |
| Psicología | `Irritability_Score` | `float64` | 0 | 1–9.3 | Irritabilidad |
| Psicología | `Restlessness_Score` | `float64` | 0 | 1.4–9 | Inquietud |
| Hábitos y actividades | `Sleep_Duration_Hours` | `float64` | 0 | 3.5–11 | Horas de sueño |
| Hábitos y actividades | `Sleep_Quality_Score` | `float64` | 0 | 3–10 | Calidad del sueño, puntuación |
| Hábitos y actividades | `Caffeine_Intake_mg` | `int64` | 0 | 0–600 | Ingesta diaria de cafeína, mg |
| Hábitos y actividades | `Exercise_Minutes` | `float64` | 370 | 0–180 | Minutos de ejercicio |
| Hábitos y actividades | `Screen_Time_Hours` | `float64` | 373 | 1–14 | Horas de pantalla |
| Hábitos y actividades | `Work_Or_Study_Hours` | `float64` | 0 | 0–18 | Horas de trabajo o estudio |
| Hábitos y actividades | `Major_Stress_Event_Today` | `object` | 0 | Yes / No | Indicador de evento estresante ese día |
| Hábitos y actividades | `Social_Interaction_Hours` | `float64` | 353 | 0–10 | Horas de interacción social |

### Notas de interpretación y reproducibilidad

Los resultados numéricos proceden del contenido íntegro del CSV asociado al objeto Git señalado arriba. Se verificaron conteos por registro y participante, campos faltantes, restricciones de formato, distribuciones y pares válidos de días consecutivos. Para los tipos numéricos se ha consignado la inferencia compatible con un cargador CSV común (por ejemplo, pandas); **no se han inventado tipos declarados por Kaggle**. La muestra es un archivo de texto con una fila por observación y valores separados por comas.

Los cálculos nuevos de correlación son **descriptivos**, no inferencia causal ni validación del comportamiento humano. No se ha estimado ningún modelo predictivo ni se ha usado el resultado de correlación para declarar un objetivo experimental. La procedencia exacta, la licencia y la fórmula de generación continúan fuera de lo que puede establecer el propio contenido del CSV.

