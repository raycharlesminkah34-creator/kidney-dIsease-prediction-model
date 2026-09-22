from enum import Enum
from pydantic import BaseModel, Field


class YesNo(str, Enum):
    yes = "yes"
    no = "no"


class NormalAbnormal(str, Enum):
    normal = "normal"
    abnormal = "abnormal"


class PresentNotPresent(str, Enum):
    present = "present"
    notpresent = "notpresent"


class GoodPoor(str, Enum):
    good = "good"
    poor = "poor"


class Patient(BaseModel):

    age: float = Field(alias="Age", ge=0, le=120)
    blood_pressure: float = Field(alias="Blood Pressure", ge=0)
    sg: float = Field(alias="SG", gt=0)
    albumin: float = Field(alias="Albumin", ge=0)
    sugar: float = Field(alias="Sugar", ge=0)

    rbc: NormalAbnormal = Field(alias="RBC")
    pus_cell: NormalAbnormal = Field(alias="Pus Cell")
    pc_clumps: PresentNotPresent = Field(alias="PC Clumps")
    bacteria: PresentNotPresent = Field(alias="Bacteria")

    random_glucose: float = Field(alias="Random Glucose", ge=0)
    blood_urea: float = Field(alias="Blood Urea", ge=0)
    creatinine: float = Field(alias="Creatinine", ge=0)
    sodium: float = Field(alias="Sodium", ge=0)
    potassium: float = Field(alias="Potassium", ge=0)
    haemoglobin: float = Field(alias="Haemoglobin", ge=0)
    pcv: float = Field(alias="PCV", ge=0)
    wbc_count: float = Field(alias="WBC Count", ge=0)
    rbc_count: float = Field(alias="RBC Count", ge=0)

    hypertension: YesNo = Field(alias="Hypertension")
    diabetes: YesNo = Field(alias="Diabetes")
    artery_disease: YesNo = Field(alias="Artery disease")
    appetite: GoodPoor = Field(alias="Appetite")
    petal_edema: YesNo = Field(alias="Petal Edema")
    anaemia: YesNo = Field(alias="Anaemia")


class PredictionResponse(BaseModel):
    prediction: str
    probability: float