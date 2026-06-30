# Build Python Backend Code

## Overview

The backend of the OptiCrop application is developed using the Flask web framework. Flask handles routing, processes user input received from HTML forms, loads the trained machine learning model, and returns crop prediction results to the user. The trained Logistic Regression model is stored as a serialized `model.pkl` file using the Pickle library and is loaded when the application starts.

The backend connects the HTML frontend with the machine learning model, enabling users to enter agricultural parameters and receive intelligent crop recommendations in real time.

---

## Objective

The objectives of this phase are to:

- Build the backend using the Flask framework.
- Load the trained machine learning model.
- Create routes for application pages.
- Process user input received from HTML forms.
- Generate crop predictions using the trained model.
- Display prediction results to users through the web interface.

---

# Step 1: Import Required Libraries

The required Python libraries are imported to create the Flask application and load the trained machine learning model.

## Python Code

```python
import numpy as np
from flask import Flask, request, render_template
import pickle
```

### Description

- **NumPy** is used for numerical array operations.
- **Flask** provides the web framework.
- **request** retrieves user input from HTML forms.
- **render_template** renders HTML pages.
- **pickle** loads the saved machine learning model.

---

# Step 2: Initialize Flask Application

The Flask application object is created and the saved machine learning model is loaded from the project directory.

## Python Code

```python
app = Flask(__name__)

path = "C:/Users/siva/Documents/Uday/Projects/Opti_Crop/"
model = pickle.load(open(path + "model.pkl", "rb"))
```

### Description

- Creates the Flask application.
- Loads the trained `model.pkl`.
- The model is ready to perform predictions without retraining.

---

# Step 3: Define Application Routes

Flask routes are created for the Home, About, and Find Your Crop pages.

## Python Code

```python
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/findyourcrop')
def findyourcrop():
    return render_template('findyourcrop.html')
```

### Description

The routes enable navigation between different pages of the application.

- `/` → Home Page
- `/about` → About Page
- `/findyourcrop` → Crop Prediction Page

---

# Step 4: Predict Crop Recommendation

The prediction route receives agricultural parameters submitted through the HTML form, converts them into numerical values, and sends them to the trained model.

## Python Code

```python
@app.route('/predict', methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]

    prediction = model.predict(features)

    output = prediction[0]

    return render_template(
        'findyourcrop.html',
        prediction_text='Best crop for given conditions is {}'.format(output)
    )
```

### Description

The prediction process includes:

- Receiving user input through a POST request.
- Converting input values into floating-point numbers.
- Creating a NumPy array.
- Passing the input to the trained model.
- Generating the predicted crop.
- Displaying the recommendation on the webpage.

---

# Step 5: Run the Flask Application

The Flask development server is started to launch the web application.

## Python Code

```python
if __name__ == "__main__":
    app.run(debug=True)
```

### Description

- Starts the Flask server.
- Enables debugging during development.
- Allows users to access the application through a web browser.

---

## Backend Workflow

The backend follows the following workflow:

1. User opens the OptiCrop application.
2. Flask renders the HTML pages.
3. User enters agricultural parameters.
4. Form data is submitted to the `/predict` route.
5. Flask converts the input into numerical values.
6. The trained Logistic Regression model predicts the most suitable crop.
7. The prediction result is sent back to the HTML page.
8. The recommended crop is displayed to the user.

---

## Input Parameters

The prediction model accepts the following agricultural features:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

---

## Output

The backend returns a crop recommendation such as:

```text
Best crop for given conditions is Coffee
```

---

## Advantages

- Simple and lightweight backend using Flask.
- Fast prediction using the saved machine learning model.
- No retraining required after deployment.
- Easy integration with HTML pages.
- Supports real-time crop recommendation.

---

## Benefits

- Provides seamless communication between frontend and machine learning model.
- Enables intelligent crop prediction based on user input.
- Supports quick and reliable agricultural recommendations.
- Simplifies deployment using the serialized model.
- Improves user experience through dynamic web pages.

---

## Conclusion

The Python backend forms the core of the OptiCrop Smart Agricultural Production Optimization Engine. Using Flask, the application efficiently connects the frontend with the trained Logistic Regression model. User-provided soil and environmental parameters are processed in real time to generate accurate crop recommendations, making the system interactive, scalable, and suitable for deployment as a smart agricultural decision-support application.
