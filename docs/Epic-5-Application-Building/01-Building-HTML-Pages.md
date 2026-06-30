
# Building HTML Pages

## Overview

The user interface of the OptiCrop Smart Agricultural Production Optimization Engine is developed using HTML to provide a simple, responsive, and user-friendly web application. The HTML pages serve as the front-end interface that enables users to navigate through different sections of the application, understand the project objectives, and obtain intelligent crop recommendations.

The application consists of three primary web pages: **Home**, **About**, and **Find Your Crop**. These pages are integrated with the Flask backend using Jinja templating (`url_for()`) to ensure seamless navigation and communication between the user interface and the machine learning prediction model.

---

## Objective

The objectives of this phase are to:

- Design a simple and responsive user interface.
- Provide easy navigation between application pages.
- Display project information and objectives.
- Collect agricultural input parameters from users.
- Connect the HTML interface with the Flask backend for crop prediction.

---

## Home Page

The **Home** page serves as the landing page of the application. It contains a navigation bar with links to the **Home**, **About**, and **Find Your Crop** pages. The page introduces the OptiCrop Smart Agricultural Production Optimization Engine and provides users with a brief overview of the application's purpose and functionality.

### HTML Code

```html
<div class="topnav">
    <a class="active" href="#home">Home</a>
    <a href="{{ url_for('about') }}">About</a>
    <a href="{{ url_for('findyourcrop') }}">FindYourCrop</a>
</div>

<div style="padding-left:16px">
    <h2>Opti Crop Agricultural Optimisation</h2>
    <p>The main purpose of the OptiCrop system is to develop an advanced software solution for intelligent crop recommendation.</p>
</div>
```

### Features

- Navigation bar
- Home page introduction
- Links to About and Find Your Crop pages
- Responsive layout

---

## About Page

The **About** page provides detailed information about the OptiCrop project. It explains how machine learning algorithms analyze soil nutrients and climatic conditions to generate accurate crop recommendations and improve agricultural productivity.

### HTML Code

```html
<div style="padding-left:16px">
    <h2>Opti Crop Smart Agricultural Optimization Using ML</h2>

    <p>
        The OptiCrop project utilizes environmental parameters such as Nitrogen,
        Phosphorous, Potassium, temperature, humidity, pH, and rainfall
        to recommend the most suitable crops using Machine Learning.
    </p>
</div>
```

### Features

- Project description
- Objectives of the system
- Importance of machine learning in agriculture
- Smart farming information

---

## Find Your Crop Page

The **Find Your Crop** page provides an interactive form that allows users to enter soil and environmental parameters required for crop prediction.

### HTML Code

```html
<form action="{{ url_for('predict') }}" method="post">

<label>Nitrogen</label>
<input type="text" name="nitrogen" required>

<label>Phosphorous</label>
<input type="text" name="phosphorous" required>

<label>Potassium</label>
<input type="text" name="potassium" required>

<label>Temperature</label>
<input type="text" name="temperature" required>

<label>Humidity</label>
<input type="text" name="humidity" required>

<label>pH</label>
<input type="text" name="ph" required>

<label>Rainfall</label>
<input type="text" name="rainfall" required>

<button type="submit">Predict</button>

</form>

<p>{{ prediction_text }}</p>
```

### Input Parameters

The form collects the following agricultural information:

- Nitrogen (N)
- Phosphorous (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

---

## HTML Components Used

The web pages include the following HTML elements:

- Navigation Bar (`<a>`)
- Div Containers (`<div>`)
- Headings (`<h2>`)
- Paragraphs (`<p>`)
- Forms (`<form>`)
- Labels (`<label>`)
- Input Fields (`<input>`)
- Submit Button (`<button>`)

---

## Workflow

The HTML application follows the workflow below:

1. User opens the Home page.
2. User navigates through the Home, About, and Find Your Crop pages.
3. Agricultural parameters are entered into the prediction form.
4. The form submits data to the Flask backend using the POST method.
5. The trained machine learning model processes the input values.
6. The predicted crop recommendation is displayed on the webpage.

---

## Benefits

- Provides a simple and interactive user interface.
- Enables smooth navigation across application modules.
- Collects agricultural data efficiently.
- Integrates seamlessly with the Flask backend.
- Displays crop prediction results in real time.
- Improves user experience through responsive web design.

---

## Conclusion

The HTML pages form the front-end interface of the OptiCrop Smart Agricultural Production Optimization Engine. They allow users to navigate the application, understand the project objectives, provide agricultural input values, and receive intelligent crop recommendations. The seamless integration between HTML and Flask enables an efficient, user-friendly, and real-time crop prediction system that supports smart and sustainable agricultural practices.
