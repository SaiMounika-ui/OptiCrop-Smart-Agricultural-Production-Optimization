
# Bivariate Analysis

## Overview

Bivariate Analysis is performed to examine the relationship between two variables in the agricultural dataset. This analysis helps identify how environmental and soil parameters influence crop recommendations. Understanding these relationships provides valuable insights for feature selection and improves the performance of machine learning models.

In this project, the relationship between **Humidity** and **Crop Labels** is analyzed using a scatter plot. The visualization illustrates how different crops are associated with varying humidity levels, enabling better understanding of environmental conditions suitable for each crop.

---

## Objective

The objectives of bivariate analysis are to:

- Study the relationship between humidity and crop labels.
- Identify crop-specific humidity requirements.
- Discover patterns that influence crop recommendation.
- Support feature selection for machine learning models.

---

## Python Code

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,8))
sns.scatterplot(x=data['humidity'], y=data['label'])

plt.title("Relationship between Humidity and Crop Labels")
plt.xlabel("Humidity (%)")
plt.ylabel("Crop")
plt.show()
```

---

## Analysis

The scatter plot displays humidity values on the X-axis and crop labels on the Y-axis. Each point represents an agricultural record in the dataset.

From the visualization, it is evident that different crops require different humidity ranges for optimal growth. Some crops such as **Rice**, **Banana**, and **Coconut** are concentrated at higher humidity levels, while crops like **Chickpea**, **Kidney Beans**, and **Lentil** are associated with comparatively lower humidity conditions.

This variation indicates that humidity is an important environmental factor in determining crop suitability and plays a significant role in the crop recommendation process.

---

## Observations

- Humidity varies significantly across different crop categories.
- High-humidity crops form distinct clusters in the dataset.
- Low-humidity crops are grouped separately, indicating different growing conditions.
- The relationship between humidity and crop type is clearly visible through the scatter plot.
- Humidity is an important predictive feature for crop recommendation.

---

## Benefits

- Helps understand relationships between environmental parameters and crop types.
- Assists in identifying significant predictive features.
- Supports exploratory data analysis before model development.
- Improves the accuracy of crop recommendation models.
- Provides insights into crop-specific environmental requirements.

---

## Conclusion

Bivariate analysis demonstrates the relationship between humidity and crop labels within the agricultural dataset. The scatter plot reveals that different crops thrive under different humidity conditions, highlighting humidity as a key feature for crop prediction. These insights contribute to better feature selection, improved model performance, and more accurate agricultural recommendations in the OptiCrop system.
