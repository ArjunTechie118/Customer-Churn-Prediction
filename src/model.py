import joblib

model = joblib.load("src/churn_lgbm_pipeline.pkl")

THRESHOLD = 0.35