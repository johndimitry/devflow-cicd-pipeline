# 🚀 DevFlow Solutions - CI/CD Enterprise Pipeline

![CI/CD](https://github.com/johndimitry/devflow-cicd-pipeline/actions/workflows/ci-cd-pipeline.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Author](https://img.shields.io/badge/Author-johndimitry-purple)

> Atividade: Pipelines CI/CD para automação de deploys - SEDUC-SP
> Implementação enterprise com 3 ambientes, testes, healthcheck e rollback automático.

**Aluno:** johndimitry | **Curso Técnico**

### 🏗️ Fluxo
Developer -> Push (develop/main) -> Build -> Test -> Deploy Homolog -> Deploy Prod (Zero Downtime)

### ✨ O que tem além do pedido
- Environments protegidos
- Deploy com rollback automático
- Docker + Gunicorn
- Healthcheck /health
- SSH com chave ED25519

### 📦 Rodar
pip install -r requirements.txt
pytest
python src/app.py