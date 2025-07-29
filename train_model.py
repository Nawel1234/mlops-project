import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

# Charger les données
df = pd.read_csv("data/iris.csv")
X = df.drop("species", axis=1)
y = df["species"]

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Démarrer le tracking MLflow
with mlflow.start_run():

    # Créer et entraîner le modèle
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Calcul de la précision
    acc = model.score(X_test, y_test)
    print(f"Accuracy: {acc}")

    # Enregistrer paramètres et métriques
    mlflow.log_param("max_iter", 200)
    mlflow.log_metric("accuracy", acc)

    # Définir la signature et exemple d'entrée
    signature = infer_signature(X_train, model.predict(X_train))
    input_example = X_train.iloc[:2]

    # Enregistrer le modèle dans l'interface MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        signature=signature,
        input_example=input_example
    )
