import pandas as pd

from src.model import model, THRESHOLD
from src.logger import logger


def create_tenure_group(df):
    df = df.copy()

    df["Tenure Group"] = pd.cut(
        df["Tenure Months"],
        bins=[-1, 12, 24, 48, float("inf")],
        labels=["0-12", "13-24", "25-48", "49+"]
    )

    return df


def predict_churn(input_data):

    logger.info("Prediction started")

    input_data = pd.DataFrame([input_data])

    input_data = create_tenure_group(input_data)

    probability = model.predict_proba(input_data)[:, 1][0]

    prediction = int(probability >= THRESHOLD)

    logger.info("Prediction completed successfully")

    return {
        "prediction": "Churn" if prediction == 1 else "No Churn",
        "churn_probability": round(float(probability), 4)
    }