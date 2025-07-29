# Projet MLOps - Déploiement d'un modèle de Machine Learning avec CI/CD et Monitoring

## 🎯 Description du projet

Dans ce projet personnel orienté MLOps, j’ai conçu et déployé un pipeline complet de machine learning intégrant les meilleures pratiques d’automatisation, de tests, de containerisation et de déploiement. Ce projet illustre mes compétences en automatisation, qualité logicielle, et industrialisation d’un modèle ML.

L’objectif principal est de rendre un modèle ML accessible via une API REST, avec une intégration continue (CI), un déploiement continu (CD), et un monitoring de performance.

---

## 🔧 Technologies utilisées

- **Python / scikit-learn** : Entraînement, évaluation et sérialisation du modèle ML.
- **MLflow** : Gestion du cycle de vie du modèle, suivi des expériences, versioning et packaging.
- **FastAPI** : Création d’une API REST rapide et moderne pour exposer le modèle.
- **Pytest** : Tests unitaires pour assurer la qualité et la robustesse du code.
- **Docker** : Containerisation de l’application pour garantir portabilité et reproductibilité.
- **GitHub Actions** : Pipeline CI/CD pour automatiser les tests et déploiements.
- **Prometheus + prometheus-fastapi-instrumentator** : Monitoring des métriques de l’API.

---

## 📌 Rôle de MLflow

MLflow est un outil clé du projet pour :

- **Suivre les expériences** : enregistrer automatiquement les paramètres, métriques et artefacts.
- **Gérer les modèles** : sauvegarder et versionner les modèles entraînés.
- **Faciliter le déploiement** : exporter le modèle dans un format réutilisable par l’API FastAPI.
- **Assurer la reproductibilité** des résultats en centralisant les informations du modèle.

---

## 🚀 Fonctionnalités principales

- Entraînement et sauvegarde du modèle Iris avec MLflow.
- API REST FastAPI pour prédire la classe d’une fleur Iris.
- Tests automatisés avec pytest.
- Containerisation Docker.
- CI/CD avec GitHub Actions déclenché à chaque push sur la branche `master`.
- Monitoring des endpoints API exposant des métriques Prometheus.

---

## 📥 Installation et utilisation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/Nawel1234/mlops-project.git
cd mlops-project
