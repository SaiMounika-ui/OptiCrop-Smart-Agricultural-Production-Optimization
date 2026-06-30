
# Run the Application

## Overview

After developing the Flask backend and HTML frontend, the OptiCrop application is executed to provide an interactive crop recommendation system. The application integrates the trained machine learning model with the web interface, allowing users to enter agricultural parameters and receive real-time crop recommendations through a web browser.

The application consists of three main pages: **Home**, **About**, and **Find Your Crop**. These pages provide project information, explain the objectives of the system, and allow users to predict the most suitable crop based on soil and environmental conditions.

---

## Objective

The objectives of this phase are to:

- Launch the Flask web application.
- Verify successful integration of the frontend and backend.
- Navigate through the application pages.
- Predict the best crop based on user-provided parameters.
- Display the prediction results in the browser.

---

# Step 1: Open the Project

Open the OptiCrop project folder in **Visual Studio Code**.

Ensure the following project files are available:

- `app.py`
- `model.pkl`
- `templates/`
- `static/`

---

# Step 2: Run the Flask Application

Open the terminal inside Visual Studio Code and execute:

```bash
python app.py
```

If the application starts successfully, the terminal displays:

```text
* Running on http://127.0.0.1:5000/
```

Open the displayed URL in your web browser.

---

# Step 3: Home Page

The Home page is displayed after launching the application.

### Features

- Navigation bar
- Project title
- Brief introduction
- Background agricultural image
- Links to other application pages

### Purpose

The Home page introduces the OptiCrop Smart Agricultural Production Optimization Engine and provides users with easy navigation throughout the application.

---

# Step 4: About Page

Click the **About** option in the navigation menu.

### Features

- Project overview
- Objectives of OptiCrop
- Importance of machine learning in agriculture
- Information about intelligent crop recommendation
- Agricultural background image

### Purpose

The About page explains how the application uses soil nutrients and environmental parameters to recommend suitable crops and improve agricultural productivity.

---

# Step 5: Find Your Crop Page

Click the **FindYourCrop** option from the navigation menu.

### Features

The prediction page contains input fields for:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

After entering all values, click the **Predict** button.

---

# Step 6: Crop Prediction

The entered values are sent to the Flask backend.

The backend performs the following operations:

1. Receives user input.
2. Converts values into numerical format.
3. Loads the trained Logistic Regression model.
4. Predicts the most suitable crop.
5. Returns the prediction to the webpage.

Example prediction:

```text
Best crop for given conditions is coffee
```

The predicted crop is displayed immediately below the prediction form.

---

## Application Workflow

The complete execution flow is:

```text
Start Application
        │
        ▼
Run app.py
        │
        ▼
Open Browser
        │
        ▼
Home Page
        │
        ▼
About Page
        │
        ▼
Find Your Crop Page
        │
        ▼
Enter Agricultural Parameters
        │
        ▼
Click Predict
        │
        ▼
Flask Backend
        │
        ▼
Machine Learning Model
        │
        ▼
Display Recommended Crop
```

---

## Input Parameters

The prediction model accepts the following agricultural parameters:

| Parameter | Description |
|------------|-------------|
| Nitrogen | Soil nitrogen content |
| Phosphorous | Soil phosphorous content |
| Potassium | Soil potassium content |
| Temperature | Environmental temperature |
| Humidity | Atmospheric humidity |
| pH | Soil pH value |
| Rainfall | Annual rainfall |

---

## Output

Example output displayed on the webpage:

```text
Best crop for given conditions is coffee
```

---

## Advantages

- User-friendly web interface.
- Real-time crop prediction.
- Fast response using the saved machine learning model.
- Easy navigation between application pages.
- Supports intelligent agricultural decision-making.

---

## Benefits

- Helps farmers select suitable crops.
- Reduces crop failure risks.
- Improves farming productivity.
- Optimizes utilization of soil nutrients and water.
- Demonstrates seamless integration of machine learning with Flask.

---

## Conclusion

The successful execution of the OptiCrop application demonstrates the integration of Flask, HTML, CSS, and the trained machine learning model into a complete web-based crop recommendation system. Users can navigate through the Home, About, and Find Your Crop pages, enter agricultural parameters, and instantly receive accurate crop recommendations, making the application an effective decision-support tool for smart and sustainable agriculture.
