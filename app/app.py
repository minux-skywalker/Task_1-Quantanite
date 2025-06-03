from fastapi import FastAPI
from pydantic import BaseModel
import torch

app= FastAPI()
class InputData(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")  # ✅ Make sure this is @app.post
def predict(data: InputData):
    return {"prediction": data.feature1 + data.feature2}
