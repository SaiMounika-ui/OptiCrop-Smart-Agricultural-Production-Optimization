
# Univariate Analysis

## Overview

Univariate Analysis is performed to examine the distribution and characteristics of each individual feature in the agricultural dataset. This analysis helps understand how each soil and environmental parameter is distributed before applying machine learning algorithms.

The agricultural parameters analyzed include Nitrogen (N), Phosphorous (P), Potassium (K), Temperature, Humidity, pH, and Rainfall. Visualizing these variables enables the identification of data patterns, skewness, variability, and potential anomalies that may influence crop recommendation accuracy.

---

## Objective

The primary objectives of univariate analysis are to:

- Understand the distribution of each agricultural feature.
- Identify the range and spread of individual variables.
- Detect skewness and unusual observations.
- Support feature understanding before preprocessing and model training.

---

## Python Code

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

plt.figure(figsize=(18,10))

for i, column in enumerate(data.columns[:-1]):
    plt.subplot(2,4,i+1)
    sns.histplot(data[column], kde=True)

plt.suptitle("Distribution of Agricultural Conditions", fontsize=18)
plt.tight_layout()
plt.show()
```

---

## Parameters Analyzed

The following features are analyzed individually:

| Feature | Description |
|----------|-------------|
| Nitrogen (N) | Nitrogen content present in the soil |
| Phosphorous (P) | Phosphorous concentration in the soil |
| Potassium (K) | Potassium content available for crop growth |
| Temperature | Average environmental temperature (°C) |
| Humidity | Relative humidity (%) |
| pH | Soil pH level |
| Rainfall | Annual rainfall (mm) |

---

## Observations

- Nitrogen values show moderate variation across different samples.
- Phosphorous values are distributed across a wide range of agricultural conditions.
- Potassium values exhibit multiple concentration levels.
- Temperature follows an approximately normal distribution.
- Humidity values are concentrated toward higher percentages.
- Soil pH values are mostly centered around neutral conditions.
- Rainfall displays noticeable variation across crop types.

---

## Benefits

- Improves understanding of individual agricultural features.
- Helps identify feature distributions before preprocessing.
- Assists in detecting abnormal values and outliers.
- Provides insights for selecting suitable machine learning algorithms.
- Supports effective feature engineering and data visualization.

---

## Conclusion

Univariate analysis provides valuable insights into the distribution of each agricultural parameter used in the OptiCrop system. Understanding these individual features improves data quality assessment and establishes a strong foundation for preprocessing, exploratory data analysis, and machine learning model development.
