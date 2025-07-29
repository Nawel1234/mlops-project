# Projet MLOps : Pipeline complet de déploiement d’un modèle de Machine Learning

## 📖 Description

Ce projet illustre la conception, l’entraînement, le déploiement et le monitoring d’un modèle de machine learning en suivant les meilleures pratiques MLOps.  
Il intègre la gestion des expériences, la containerisation, les tests automatisés, l’intégration continue/déploiement continu (CI/CD) ainsi que le monitoring applicatif.

## ⚙️ Architecture & Technologies

- **Python & scikit-learn** : Modélisation et entraînement d’un classifieur de fleurs Iris  
- **MLflow** : Gestion et suivi des expériences, métriques et modèles  
- **FastAPI** : Développement d’une API REST performante pour la prédiction  
- **Docker** : Containerisation de l’application pour portabilité et scalabilité  
- **GitHub Actions** : Pipeline CI/CD pour automatiser tests et déploiement  
- **Pytest** : Assurance qualité via tests unitaires  
- **Prometheus & prometheus-fastapi-instrumentator** : Monitoring et métriques applicatives exposées pour intégration avec outils de supervision  

## 🚀 Fonctionnalités clés

- Entraînement reproductible avec traçabilité complète des métriques grâce à MLflow  
- API REST légère et performante pour servir le modèle en production  
- Pipeline CI/CD automatisé garantissant la robustesse du code  
- Monitoring intégré pour suivi en temps réel de la santé de l’application  
- Code modulaire, maintenable et extensible  

## 💾 Installation & Usage

```bash
git clone https://github.com/Nawel1234/mlops-project.git
cd mlops-project
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows PowerShell
pip install -r requirements.txt


## 🚀 Entraînement du modèle

python train_model.py

## 🚀 Démarrer l’API FastAPI

uvicorn app.main:app --reload
L’API sera accessible sur http://127.0.0.1:8000.

## Exécution des tests unitaires
pytest

🔧 CI/CD & Monitoring

Le pipeline GitHub Actions automatise la construction, les tests, et le déploiement continu

Les métriques Prometheus sont exposées via l’API, prêtes à être intégrées dans un tableau de bord de monitoring