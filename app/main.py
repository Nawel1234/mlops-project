import os
from fastapi import FastAPI
from app.schema import IrisRequest, IrisResponse
from app.utils import ModelLoader

app = FastAPI(
    title="Iris Classifier API",
    description="API de prédiction de fleurs Iris avec un modèle MLflow",
    version="1.0"
)

# Construire le chemin absolu vers le modèle
model_dir = os.path.abspath("model/logistic_regression_model")
model_dir = model_dir.replace("\\", "/")  # pour éviter problème sur Windows
model_loader = ModelLoader(model_dir)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Iris Classifier"}

@app.post("/predict", response_model=IrisResponse)
def predict_iris(data: IrisRequest):
    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]
    prediction = model_loader.predict(features)
    return IrisResponse(prediction=prediction)
