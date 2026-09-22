from fastapi import FastAPI
import pandas as pd
from enum import Enum
from api.schemas import PredictionResponse, Patient
from api.model import model


app = FastAPI()

@app.get("/")
def home():
    return {"message": "CKD Prediction API is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(patient: Patient):
    patient_data = patient.model_dump(by_alias=True)
    patient_df = pd.DataFrame([patient_data])

    prediction = model.predict(patient_df)[0]
    probability = model.predict_proba(patient_df)[0][0]

    

    return {
        "prediction": prediction,
        "probability": float(probability)
    }


