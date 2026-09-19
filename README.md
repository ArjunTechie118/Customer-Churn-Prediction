<div align="center">

# 🎯 ChurnIQ

### AI-Powered Churn Intelligence

*Predict customer churn before it happens.*

[![Python](https://img.shields.io/badge/Python-3.14.6-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=flat)](https://lightgbm.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Live Demo](https://customer-churn-prediction-lgbm.streamlit.app/) · [Report Bug](../../issues)

</div>

---

ChurnIQ is an end-to-end machine learning application designed to predict customer churn and identify customers who may be at risk of leaving.

The project goes beyond model training by combining a machine learning model with a **FastAPI** backend, **Streamlit** frontend, and cloud deployment to create a complete, usable ML product.

---

## 🚀 Project Overview

Customer churn is a common business challenge. Identifying customers who are likely to leave can help businesses take action before they churn.

ChurnIQ takes customer information as input and uses a trained **LightGBM** classification model to generate:

- Churn prediction
- Churn probability
- Customer risk level

The application provides a simple interface where users can enter customer details and receive a prediction through the deployed ML system.

---

## ✨ Features

| | Feature |
|---|---|
| 🤖 | Customer churn prediction using Machine Learning |
| 📊 | Churn probability estimation |
| 🚦 | Low, Medium, and High risk classification |
| 🎨 | Interactive Streamlit frontend |
| ⚡ | FastAPI REST API for model inference |
| ✅ | Input validation using Pydantic |
| 🔄 | End-to-end ML pipeline |
| ☁️ | Cloud-deployed application |
| 🧩 | API and frontend separated into independent components |

---

## 🧠 How ChurnIQ Works

```text
Customer Information
        ↓
Data Processing
        ↓
LightGBM Classification Model
        ↓
Churn Probability
        ↓
Churn / No Churn Prediction
        ↓
Risk Level
```

### Risk Classification

| Risk Level | Churn Probability | Suggested Action |
|:---|:---|:---|
| 🟢 **Low** | `0.00 – 0.39` | Monitor normally |
| 🟡 **Medium** | `0.40 – 0.69` | Proactive engagement |
| 🔴 **High** | `0.70 – 1.00` | Immediate retention outreach |

---

## 🛠️ Tech Stack

- Python
- LightGBM
- scikit-learn
- pandas
- NumPy
- Matplotlib
- Seaborn
- FastAPI
- Pydantic
- Uvicorn
- Streamlit

---

## 📁 Project Structure

```text
Churn-Prediction/
│
├── frontend/
│   ├── streamlit_app.py
│   │
│   └── pages/
│       ├── home.py
│       ├── predict.py
│       └── about.py
│
├── src/
│   ├── model.py
│   ├── prediction.py
│   ├── schemas.py
│   ├── logger.py
│   └── churn_lgbm_pipeline.pkl
│
├── modelling/
│   ├── model_training.ipynb
│   └── final_pipeline.ipynb
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ArjunTechie118/Customer-Churn-Prediction.git/
cd ChurnIQ
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the backend and frontend in **two separate terminals**.

**Terminal 1 — FastAPI backend**

```bash
uvicorn api.main:app --reload --port 8000
```

API available at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

**Terminal 2 — Streamlit frontend**

```bash
streamlit run app/streamlit_app.py
```

Frontend available at `http://localhost:8501`

---

## 🔌 API Reference

### `POST /predict`

Returns a churn prediction for a single customer.

**Request**

```json
{
  "tenure": 12,
  "monthly_charges": 79.85,
  "total_charges": 958.2,
  "contract": "Month-to-month",
  "internet_service": "Fiber optic",
  "payment_method": "Electronic check"
}
```

**Response**

```json
{
  "churn_prediction": 1,
  "churn_probability": 0.82,
  "risk_level": "High"
}
```

### `GET /health`

Health check endpoint for uptime monitoring.

```json
{ "status": "healthy" }
```

---

## 📈 Model Performance

| Metric | Score |
|:---|:---|
| Accuracy | `79.55%` |
| Precision | `60.28%` |
| Recall | `67.37%` |
| F1 Score | `63.60%` |
| ROC-AUC | `85.21%` |

> Replace with your actual evaluation results from the test set.

---

## 🗺️ Roadmap

- [ ] Batch prediction via CSV upload
- [ ] Model monitoring and drift detection
- [ ] Automated retraining pipeline
- [ ] Authentication for the API

---

## Future Roadmap

**From Predicting Churn to Helping Prevent Customer Loss**

The next phase of ChurnIQ will integrate SHAP explainability, company policies, and an LLM + RAG system to generate grounded customer-retention recommendations.

**Current:** ML-based churn prediction → **Future:** AI-powered retention recommendations

- Churn Prediction
- SHAP / Key Factors
- Company Policies
- LLM + RAG
- Retention Recommendation
```

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

**Built with ❤️ by [Your Name](https://github.com/<your-username>)**

⭐ Star this repo if you found it useful

</div>