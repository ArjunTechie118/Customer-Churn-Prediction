# ChurnIQ

### AI-Powered Churn Intelligence

ChurnIQ is an end-to-end machine learning application designed to predict customer churn and identify customers who may be at risk of leaving.

The project goes beyond model training by combining a machine learning model with a FastAPI backend, Streamlit frontend, and cloud deployment to create a complete, usable ML product.

---
## 🚀 Project Overview

Customer churn is a common business challenge. Identifying customers who are likely to leave can help businesses take action before they churn.

ChurnIQ takes customer information as input and uses a trained LightGBM classification model to generate:

- Churn prediction
- Churn probability
- Customer risk level

The application provides a simple interface where users can enter customer details and receive a prediction through the deployed ML system.

---

## ✨ Features

- Customer churn prediction using Machine Learning
- Churn probability estimation
- Low, Medium, and High risk classification
- Interactive Streamlit frontend
- FastAPI REST API for model inference
- Input validation using Pydantic
- End-to-end ML pipeline
- Cloud-deployed application
- API and frontend separated into independent components

---

## 🧠 How ChurnIQ Works
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

## 🤖 Machine Learning
Model

LightGBM Classifier

LightGBM was selected as the classification model for predicting whether a customer is likely to churn.

The model works with customer demographic, service, contract, and billing-related information.

Prediction Output

The model produces:

Prediction → Churn / No Churn
Probability → Churn probability

The application then uses the prediction probability to determine the customer's risk level.

## 📊 Input Features

ChurnIQ uses customer information such as:

Customer Profile
Senior Citizen
Partner
Dependents
Tenure Months
Service Information
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Contract & Billing
Contract
Paperless Billing
Payment Method
Monthly Charges
Total Charges


## 🏗️ Technology Stack

Python	
Pandas	
NumPy	
Scikit-learn	
LightGBM	
FastAPI	
Pydantic	
Streamlit	
Git & GitHub	
Render


## 🔌 Deployment Architecture

┌──────────────────────┐
│   Streamlit Frontend │
│     User Interface   │
└──────────┬───────────┘
           │
           │ REST API
           ↓
┌──────────────────────┐
│    FastAPI Backend   │
│       /predict       │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│   LightGBM Model     │
│   Churn Prediction   │
└──────────┬───────────┘
           │
           ↓
┌──────────────────────┐
│    API Response      │
│ Prediction +         │
│ Churn Probability    │
└──────────────────────┘


## 📁 Project Structure

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


## 🔗 API

ChurnIQ uses FastAPI to expose the trained ML model through a REST API.

Health Check
GET /health

Used to verify that the API is running.

Prediction
POST /predict

The endpoint accepts customer information and returns:

{
  "prediction": "Churn",
  "churn_probability": 0.78
}


## 💻 Run Locally
1. Clone the repository:

git clone https://github.com/ArjunTechie118/Customer-Churn-Prediction.git

cd Customer-Churn-Prediction

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Run the FastAPI backend:
uvicorn app:app --reload

The API will be available at:

http://127.0.0.1:8000

6. Run the Streamlit frontend

From the frontend directory:
streamlit run frontend/streamlit_app.py

## 🌐 Live Application

The project is deployed and available online.
Live ChurnIQ: https://customer-churn-prediction-lgbm.streamlit.app/

GitHub Repository

https://github.com/ArjunTechie118/Customer-Churn-Prediction

## 🛣️ Future Roadmap

SHAP Explainability

Add SHAP-based explainability to show which customer features contribute most to an individual churn prediction.

LLM + RAG for Retention Recommendations

Extend ChurnIQ with an LLM and RAG pipeline to generate personalized, context-aware customer retention recommendations grounded in relevant business policies and guidelines.

The goal is to move from:

Predict Churn
      ↓
Understand Risk
      ↓
Recommend Retention Action

This would extend ChurnIQ from a churn prediction system toward a more complete customer retention intelligence workflow.

## 🎯 Project Goals

ChurnIQ was built to demonstrate an end-to-end approach to machine learning engineering:

Data
 ↓
Preprocessing
 ↓
Model Development
 ↓
Prediction Pipeline
 ↓
FastAPI
 ↓
Streamlit
 ↓
Deployment

The project focuses on taking a machine learning model beyond experimentation and turning it into a practical application.

## 👨‍💻 Author

Arjun

An AI/ML Engineer passionate about building practical, end-to-end machine learning products that go beyond just model training

GitHub:

https://github.com/ArjunTechie118

## ⭐ If you found this project interesting

Feel free to explore the repository and follow the project as new capabilities are added.


### One important change I'd make before you paste it

Your **Project Structure** in the README should match your actual GitHub repository exactly. I know your repo currently has `data`, `frontend`, `images`, `modelling`, `notebook`, `src`, `app.py`, `requirements.txt`, `setup.py`, etc., but I don't want to invent files inside those folders.

If you want, I can also :contentReference[oaicite:0]{index=0}—while keeping every claim a