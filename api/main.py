from fastapi import FastAPI
import pandas as pd
from api.schemas import PredictionResponse, Patient
from api.model import model


try:
    app = FastAPI(
        title="CKD Prediction API",
        description= "API for predicting Chronic Kidney Disease",
        version="1.0.0"
    )

    @app.get("/")
    def home():
        return {"message": "CKD Prediction API is running"}

    @app.post("/predict", response_model=PredictionResponse)
    def predict(patient: Patient):
        patient_data = patient.model_dump(by_alias=True, mode="json")
        patient_df = pd.DataFrame([patient_data])

        prediction = model.predict(patient_df)[0]
        probability = model.predict_proba(patient_df)[0][0]


        return {
            "prediction": prediction,
            "probability": float(probability)
        }

except Exception as e:
    print(f"ERROR: {repr(e)}")
    raise
