from fastapi import FastAPI, HTTPException
from src.schemas import UserInput, PredictionResponse
from src.schemas import UserInput
from src.prediction import predict_churn
from src.logger import logger


app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn using a trained LightGBM model.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my Customer Churn Prediction project"
    }


@app.post("/predict",response_model=PredictionResponse)
def predict(data: UserInput):

    logger.info("Prediction request received")

    try:
        input_data = data.model_dump(by_alias=True)

        result = predict_churn(input_data)

        return result

    except Exception:
        logger.exception("Prediction failed")

        raise HTTPException(
            status_code=500,
            detail="An error occurred while making the prediction."
        )