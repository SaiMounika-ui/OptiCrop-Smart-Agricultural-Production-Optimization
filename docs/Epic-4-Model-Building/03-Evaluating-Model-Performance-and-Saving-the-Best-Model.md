# Evaluating Model Performance and Saving the Best Model

## Overview

After training the machine learning models, their performance is evaluated using standard classification metrics. These metrics help determine how accurately the model predicts suitable crops based on agricultural and environmental parameters.

In the OptiCrop system, the trained Logistic Regression model is evaluated using the **Classification Report**, which includes Precision, Recall, F1-Score, and Accuracy for each crop category. Based on the evaluation results, the best-performing model is selected and saved as a serialized file (`model.pkl`) using the Pickle library. This saved model can later be loaded directly into the Flask web application without requiring retraining.

---

## Objective

The objectives of this phase are to:

- Evaluate the performance of the trained machine learning model.
- Measure prediction accuracy using standard classification metrics.
- Compare model performance to select the best algorithm.
- Save the finalized model for deployment.

---

## Python Code

### Generate Classification Report

```python
from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred)

print(report)
```

### Save the Best Model

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

### Load the Saved Model

```python
model = pickle.load(open("model.pkl", "rb"))
```

---

## Performance Metrics

The Classification Report evaluates the model using the following metrics:

### Precision

Precision measures how many of the predicted crop labels are actually correct.

```
Precision = TP / (TP + FP)
```

---

### Recall

Recall measures how many actual crop labels are correctly identified by the model.

```
Recall = TP / (TP + FN)
```

---

### F1-Score

The F1-Score is the harmonic mean of Precision and Recall.

```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

---

### Accuracy

Accuracy represents the percentage of correctly classified crop predictions.

```
Accuracy = Correct Predictions / Total Predictions
```

---

## Sample Output

The Classification Report displays evaluation results for all crop categories, including:

- Precision
- Recall
- F1-Score
- Support

Overall model performance:

```
Accuracy : 94%

Macro Average Precision : 95%
Macro Average Recall    : 95%
Macro Average F1-Score  : 95%

Weighted Average Precision : 95%
Weighted Average Recall    : 94%
Weighted Average F1-Score  : 94%
```

---

## Analysis

The evaluation report indicates that the Logistic Regression model performs effectively in classifying different crop types. Most crop categories achieve high precision and recall values, demonstrating that the model has learned meaningful relationships between soil nutrients, climatic conditions, and crop suitability.

The overall accuracy of approximately **94%** shows that the model is reliable for intelligent crop recommendation.

---

## Observations

- The model achieves approximately **94% prediction accuracy**.
- Most crop classes obtain high Precision and Recall values.
- The F1-Score indicates balanced classification performance.
- Weighted and Macro averages confirm stable model performance.
- The trained model is suitable for deployment in the web application.

---

## Saving the Best Model

After evaluation, the best-performing model is serialized using the **Pickle** library.

The saved model file:

```
model.pkl
```

Advantages of saving the model:

- Eliminates the need for retraining every time the application starts.
- Reduces application loading time.
- Enables seamless integration with the Flask backend.
- Supports efficient deployment and real-time crop prediction.

---

## Benefits

- Provides objective evaluation of model performance.
- Identifies the most accurate prediction model.
- Supports reliable crop recommendation.
- Enables faster deployment using a saved model.
- Improves scalability and maintainability of the application.

---

## Conclusion

Model evaluation is an essential step in the OptiCrop system to ensure accurate and reliable crop recommendations. Using classification metrics such as Precision, Recall, F1-Score, and Accuracy, the Logistic Regression model demonstrates strong predictive performance with an overall accuracy of approximately **94%**. The finalized model is then saved as **model.pkl**, allowing it to be reused efficiently within the Flask-based web application for real-time agricultural prediction.
