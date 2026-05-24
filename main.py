from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HouseFeatures(BaseModel):
    area: float
    distance: float
    

@app.post("/predict")
def predict_price(features: HouseFeatures):

    price = 200 +15*features.area-10*features.distance
    return {"predicted_price": price}