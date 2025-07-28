from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API MLOps !"}

def test_predict_post_success():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], str)

def test_predict_post_missing_field():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4
        # petal_width manquant
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Validation error de FastAPI
