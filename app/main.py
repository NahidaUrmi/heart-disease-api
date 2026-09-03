
from fastapi import FastAPI
import joblib
import pandas as pd

from app.schemas import HeartDiseaseInput


# Load trained model
model = joblib.load("model/heart_model.joblib")


# Create FastAPI application
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting heart disease using a Logistic Regression model.",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {
        "model": "Logistic Regression",
        "dataset": "Heart Disease Dataset",
        "features": 13
    }


@app.post("/predict")
def predict(data: HeartDiseaseInput):

    input_data = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "cp": data.cp,
        "trestbps": data.trestbps,
        "chol": data.chol,
        "fbs": data.fbs,
        "restecg": data.restecg,
        "thalach": data.thalach,
        "exang": data.exang,
        "oldpeak": data.oldpeak,
        "slope": data.slope,
        "ca": data.ca,
        "thal": data.thal
    }])

    prediction = model.predict(input_data)[0]

    return {
        "heart_disease": bool(prediction)
    }

