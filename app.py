from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Literal,Optional
from pydantic import BaseModel,Field,computed_field
import joblib

#load model
model = joblib.load("src/churn_xgb_pipeline.pkl")

app = FastAPI()

