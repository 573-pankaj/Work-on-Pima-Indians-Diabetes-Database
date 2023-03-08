from pydantic import BaseModel
# 2. Class which describes Diabetes measurements
class diabetesPrediction(BaseModel):
    Pregnancies: int 
    Glucose: int
    BloodPressure: int 
    SkinThickness: int
    Insulin: int
    BMI  : float
    DiabetesPedigreeFunction: float
    Age: int