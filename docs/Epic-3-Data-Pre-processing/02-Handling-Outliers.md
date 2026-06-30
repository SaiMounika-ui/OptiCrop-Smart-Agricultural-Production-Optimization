# Handling Outliers

## Overview

Outlier detection is an important preprocessing step that helps identify abnormal or extreme values in the dataset. These unusual observations can negatively affect machine learning model performance, resulting in inaccurate crop recommendations. Therefore, outliers are detected and treated before model training.

In the OptiCrop system, boxplots are used to visually identify outliers, while the Interquartile Range (IQR) method is applied to calculate the acceptable range of values for each numerical feature.

---

## Objective

The objectives of outlier handling are to:

- Detect extreme values in agricultural features.
- Improve data quality and consistency.
- Reduce the influence of abnormal observations.
- Enhance machine learning model performance and prediction accuracy.

---

## Python Code

### Visualizing Outliers

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,4))
sns.boxplot(data=data)

plt.title("Boxplot for Agricultural Features")
plt.show()
```

### Detecting Outliers Using IQR

```python
Q1 = data['phosphorous'].quantile(0.25)
Q3 = data['phosphorous'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered = (data['phosphorous'] >= lower_bound) & (data['phosphorous'] <= upper_bound)

data = data.loc[filtered]
```

---

## Interquartile Range (IQR)

The IQR method identifies outliers using the following formulas:

- **Lower Bound = Q1 − 1.5 × IQR**
- **Upper Bound = Q3 + 1.5 × IQR**

Where:

- **Q1** = First Quartile (25%)
- **Q3** = Third Quartile (75%)
- **IQR = Q3 − Q1**

Values outside these limits are considered outliers.

---

## Observations

- Boxplots reveal the presence of outliers in several agricultural features.
- Potassium and rainfall exhibit noticeable extreme values.
- The IQR technique effectively identifies observations outside the normal range.
- Filtering or transforming these values improves dataset consistency.
- The cleaned dataset becomes more suitable for machine learning algorithms.

---

## Benefits

- Improves data quality.
- Reduces the impact of extreme values.
- Enhances model stability and prediction accuracy.
- Produces better feature distributions.
- Supports robust crop recommendation performance.

---

## Conclusion

Outlier handling is a critical preprocessing step in the OptiCrop system. By combining boxplot visualization with the Interquartile Range (IQR) method, abnormal observations are identified and treated effectively. This process improves the reliability of the dataset and contributes to more accurate crop prediction and intelligent agricultural decision-making.
