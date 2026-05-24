
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_predict_endpoind():

    response=client.post("/predict", json={"area":100.0,"distance":10.0})

    data = response.json()

    assert response.status_code == 200

    assert data["predicted_price"] == 1600.0, "Код працює некоректно"  
    
    
