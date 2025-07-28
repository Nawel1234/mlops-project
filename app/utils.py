import pandas as pd
import mlflow.pyfunc

class ModelLoader:
    def __init__(self, model_path: str):
        print(f"Chargement du modèle depuis : {model_path}")
        self.model = mlflow.pyfunc.load_model(model_path)
        print("Modèle chargé avec succès")

    def predict(self, features: list) -> str:
        # Créer un DataFrame avec les bons noms de colonnes
        df = pd.DataFrame([features], columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
        prediction = self.model.predict(df)
        return prediction[0]
