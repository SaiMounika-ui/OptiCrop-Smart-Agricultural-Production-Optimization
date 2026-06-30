
# Splitting Data into Train and Test Sets

## Overview

Splitting the dataset into training and testing sets is an essential preprocessing step in machine learning. It enables the model to learn from one portion of the data and evaluate its performance on unseen data. This helps assess the model's ability to generalize and make accurate crop predictions.

In the OptiCrop system, the dataset is divided into feature variables (**X**) and the target variable (**y**). The `train_test_split()` function from Scikit-learn is then used to create separate training and testing datasets.

---

## Objective

The objectives of this step are to:

- Separate input features and target labels.
- Prepare data for machine learning model training.
- Evaluate model performance on unseen data.
- Prevent overfitting and improve prediction reliability.

---

## Python Code

```python
# Separate features and target variable

y = data['label']
X = data.drop(['label'], axis=1)

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0
)

print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)
```

---

## Sample Output

```
Shape of X: (2062, 7)
Shape of y: (2062,)

Shape of X_train: (1649, 7)
Shape of X_test: (413, 7)
Shape of y_train: (1649,)
Shape of y_test: (413,)
```

---

## Analysis

The agricultural dataset is divided into two parts:

- **Training Set (80%)** – Used to train the machine learning model.
- **Testing Set (20%)** – Used to evaluate the trained model on unseen data.

The feature matrix (**X**) contains seven agricultural parameters:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

The target variable (**y**) contains the crop labels that the model is trained to predict.

---

## Observations

- The dataset contains **2062 samples** after preprocessing.
- Seven input features are used for model training.
- The target variable consists of crop labels.
- The training dataset contains **1649 samples**.
- The testing dataset contains **413 samples**.
- An **80:20** split provides sufficient data for both training and evaluation.

---

## Benefits

- Enables effective machine learning model training.
- Prevents overfitting by evaluating the model on unseen data.
- Improves prediction accuracy and reliability.
- Supports fair performance evaluation.
- Provides a standardized workflow for model development.

---

## Conclusion

Splitting the dataset into training and testing sets is a fundamental step in developing the OptiCrop crop recommendation system. By separating the feature variables from the target labels and using an 80:20 train-test split, the model can be trained efficiently and evaluated objectively. This approach improves the reliability, accuracy, and generalization capability of the crop recommendation model.
