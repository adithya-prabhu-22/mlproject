from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import os
import pickle

application = Flask(__name__)
app = application

MODEL_PATH = os.path.join("artifacts", "model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("home.html")

    try:
        data = {
            "gender": request.form["gender"],
            "race/ethnicity": request.form["race/ethnicity"],
            "parental level of education": request.form["parental level of education"],
            "lunch": request.form["lunch"],
            "test preparation course": request.form["test preparation course"],
            "reading score": float(request.form["reading score"]),
            "writing score": float(request.form["writing score"]),
        }

        input_df = pd.DataFrame([data])

        with open(PREPROCESSOR_PATH, "rb") as f:
            preprocessor = pickle.load(f)

        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)

        transformed_data = preprocessor.transform(input_df)
        prediction = model.predict(transformed_data)[0]

        return render_template(
            "home.html",
            prediction_text=f"Predicted Math Score: {round(prediction, 2)}"
        )

    except Exception as e:
        return render_template(
            "home.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
