# Logistic Regression

## Overview

Logistic Regression is a supervised machine learning algorithm used for classification tasks. In the OptiCrop system, it is implemented to predict the most suitable crop based on agricultural and environmental parameters such as Nitrogen (N), Phosphorous (P), Potassium (K), temperature, humidity, pH, and rainfall.

The model is trained using the prepared training dataset and later used to generate crop predictions for unseen testing data. This approach enables intelligent crop recommendation by learning the relationship between environmental conditions and crop labels.

---

## Objective

The objectives of this phase are to:

- Train a classification model using agricultural data.
- Predict the most suitable crop for given environmental conditions.
- Learn patterns between soil parameters and crop labels.
- Prepare the model for evaluation and deployment.

---

## Python Code

### Import Library

```python
from sklearn.linear_model import LogisticRegression
```

### Train the Logistic Regression Model

```python
model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

---

## Working Principle

The Logistic Regression algorithm learns the relationship between the input features and crop labels using the training dataset. Once the model is trained, it predicts the most appropriate crop for new agricultural conditions by classifying the input into one of the available crop categories.

The model uses the following agricultural features:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

The target variable is:

- Crop Label

---

## Model Training

The dataset is divided into:

- **Training Set (80%)** – Used to train the Logistic Regression model.
- **Testing Set (20%)** – Used to evaluate prediction performance.

The model is trained using:

```python
model.fit(X_train, y_train)
```

Predictions are generated using:

```python
y_pred = model.predict(X_test)
```

---

## Observations

- Logistic Regression successfully learns the relationship between agricultural features and crop labels.
- The model generates crop predictions for unseen data.
- Prediction accuracy depends on data quality and preprocessing.
- Proper feature scaling and sufficient iterations improve model convergence.
- The trained model serves as the foundation for crop recommendation.

---

## Convergence Warning

During training, the following warning may appear:

```
ConvergenceWarning:
lbfgs failed to converge (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT.
```

This warning indicates that the optimization algorithm reached the maximum number of iterations before fully converging. It can be resolved by:

- Increasing the `max_iter` value.
- Applying feature scaling using `StandardScaler`.
- Choosing an alternative solver if required.

Example:

```python
model = LogisticRegression(max_iter=1000)
```

---

## Benefits

- Simple and efficient classification algorithm.
- Fast model training and prediction.
- Works well for multiclass crop classification.
- Easy to interpret and implement.
- Suitable as a baseline model for crop recommendation.

---

## Conclusion

Logistic Regression is implemented in the OptiCrop system to classify agricultural conditions and recommend the most suitable crop. The model is trained using historical agricultural data and generates predictions based on soil nutrients and climatic conditions. After training, the model is ready for performance evaluation, allowing its effectiveness in crop recommendation to be assessed before deployment.
