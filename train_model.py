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

# Dossier de sauvegarde du modèle
model_save_path = "model/logistic_regression_model"

# Créer le dossier s'il n'existe pas
os.makedirs(model_save_path, exist_ok=True)

# Entraîner et sauvegarder le modèle avec MLflow
with mlflow.start_run():
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Accuracy: {acc}")
    mlflow.log_metric("accuracy", acc)

    signature = infer_signature(X_train, model.predict(X_train))
    input_example = X_train.iloc[:2]

    mlflow.sklearn.save_model(
        sk_model=model,
        path=model_save_path,
        signature=signature,
        input_example=input_example,
    )
