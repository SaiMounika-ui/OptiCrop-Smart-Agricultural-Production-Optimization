# Extracting Seasonal Crops

## Overview

Extracting seasonal crops is an important preprocessing step in the OptiCrop system. Crops are categorized based on environmental conditions such as temperature, humidity, and rainfall to determine their suitability for different seasons. This analysis enables the system to provide season-specific crop recommendations, improving agricultural planning and decision-making.

The dataset is filtered using predefined threshold values for temperature, humidity, and rainfall to identify crops that are best suited for summer, winter, and rainy seasons.

---

## Objective

The objectives of this step are to:

- Categorize crops based on seasonal conditions.
- Identify crops suitable for summer, winter, and rainy seasons.
- Analyze environmental factors affecting crop growth.
- Improve the accuracy of crop recommendation.

---

## Python Code

```python
print("Summer Crops")
print(data[(data['temperature'] > 30) &
           (data['humidity'] > 50)]['label'].unique())

print("------------------------------------------")

print("Winter Crops")
print(data[(data['temperature'] < 20) &
           (data['humidity'] > 30)]['label'].unique())

print("------------------------------------------")

print("Rainy Crops")
print(data[(data['rainfall'] > 200) &
           (data['humidity'] > 50)]['label'].unique())
```

---

## Sample Output

### Summer Crops

- Pigeonpeas
- Mothbeans
- Blackgram
- Mango
- Grapes
- Orange
- Papaya

### Winter Crops

- Maize
- Pigeonpeas
- Lentil
- Pomegranate
- Grapes
- Orange

### Rainy Crops

- Rice
- Papaya
- Coconut

---

## Analysis

The agricultural dataset is filtered using environmental thresholds to classify crops into different seasonal categories.

- **Summer crops** are selected based on high temperature and humidity conditions.
- **Winter crops** are identified using lower temperatures and moderate humidity levels.
- **Rainy crops** are selected based on high rainfall and humidity.

These conditions simulate seasonal agricultural environments and help determine the most suitable crops for cultivation during each season.

---

## Observations

- Different crops require different environmental conditions for optimal growth.
- Summer crops generally prefer higher temperatures and humidity.
- Winter crops grow well in cooler climatic conditions.
- Rainy crops require high rainfall and moisture availability.
- Seasonal classification improves crop recommendation accuracy.

---

## Benefits

- Supports season-wise crop recommendation.
- Helps farmers select suitable crops for different climatic conditions.
- Improves agricultural productivity.
- Enables better utilization of soil and environmental resources.
- Enhances the performance of the crop recommendation system.

---

## Conclusion

Seasonal crop extraction enables the OptiCrop system to classify crops according to temperature, humidity, and rainfall conditions. This analysis supports intelligent farming decisions by recommending crops that are most suitable for specific seasons. The extracted seasonal information enhances prediction accuracy and contributes to sustainable and efficient agricultural practices.
