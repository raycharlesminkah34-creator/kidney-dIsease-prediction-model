from fastapi.testclient import TestClient
from api.main import app
import pytest

@pytest.fixture
def valid_patient():
    return {
            "Age": 55,
            "Blood Pressure": 80,
            "SG": 1.015,
            "Albumin": 2,
            "Sugar": 0,
            "RBC": "normal",
            "Pus Cell": "normal",
            "PC Clumps": "notpresent",
            "Bacteria": "notpresent",
            "Random Glucose": 143,
            "Blood Urea": 53,
            "Creatinine": 2.25,
            "Sodium": 136,
            "Potassium": 4.5,
            "Haemoglobin": 10.9,
            "PCV": 33,
            "WBC Count": 8000,
            "RBC Count": 3.8,
            "Hypertension": "yes",
            "Diabetes": "yes",
            "Artery disease": "no",
            "Appetite": "good",
            "Petal Edema": "no",
            "Anaemia": "yes"
        }

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "CKD Prediction API is running"
    }

def test_prediction(valid_patient):

    response = client.post("/predict", json=valid_patient)
    assert response.status_code == 200

def test_prediction_response(valid_patient):

    response = client.post("/predict", json=valid_patient)
    assert response.status_code == 200
    assert response.json()["prediction"]
    assert response.json()["probability"]
    assert response.json()["prediction"] in ["ckd", "notckd"]
    assert 0 <= response.json()["probability"] <= 1


def test_invalid_patient(valid_patient):
    patient = valid_patient.copy()
    patient["Age"] = 150
    response = client.post("/predict", json=patient)
    assert response.status_code == 422


def test_missing_field(valid_patient):
    patient = valid_patient.copy()
    patient.pop("Creatinine", None)
    
    response = client.post("/predict", json=patient)
    assert response.status_code == 422


