# import numpy as np
# import pickle
# from flask import Flask, render_template, request

# app = Flask(__name__)

# # Load the trained model
# model = pickle.load(open("model.pkl", "rb"))

# # Home Page
# @app.route('/')
# def home():
#     return render_template("home.html")

# # About Page
# @app.route('/about')
# def about():
#     return render_template("about.html")

# # Find Your Crop Page
# @app.route('/findyourcrop')
# def findyourcrop():
#     return render_template("findyourcrop.html")

# # Prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         features = [float(x) for x in request.form.values()]
#         final_features = [np.array(features)]

#         prediction = model.predict(final_features)
#         output = prediction[0]

#         return render_template(
#             "findyourcrop.html",
#             prediction_text=f"Best crop for given conditions is {output}"
#         )

#     except Exception as e:
#         return render_template(
#             "findyourcrop.html",
#             prediction_text="Invalid Input! Please enter valid numbers."
#         )


# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request
import numpy as np
import pickle

# Create Flask App
app = Flask(__name__)

# Load Trained Model
model = pickle.load(open("model.pkl", "rb"))

# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Find Your Crop Page
@app.route("/findyourcrop")
def findyourcrop():
    return render_template("findyourcrop.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        N = float(request.form["Nitrogen"])
        P = float(request.form["Phosphorous"])
        K = float(request.form["Potassium"])
        temperature = float(request.form["Temperature"])
        humidity = float(request.form["Humidity"])
        ph = float(request.form["pH"])
        rainfall = float(request.form["Rainfall"])

        # Prepare input
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

        # Predict crop
        prediction = model.predict(data)

        crop = prediction[0]

        # Show result page
        return render_template(
            "result.html",
            prediction=crop,
            N=N,
            P=P,
            K=K,
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall
        )

    except Exception as e:
        return render_template("result.html", prediction=f"Error: {e}")


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)