
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Sales Conversion Prediction",
    description="Predict website visitor purchase likelihood",
    version="1.0.0",
)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

MODEL_PATH = Path(__file__).parent / "sales_conversion_model.pkl"
artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
threshold = artifact["threshold"]
features = artifact["features"]

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]
VISITOR_TYPES = ["Returning_Visitor", "New_Visitor", "Other"]
DEFAULT_VALUES = {
    "Administrative": 2,
    "Administrative_Duration": 50,
    "Informational": 1,
    "Informational_Duration": 20,
    "ProductRelated": 3,
    "ProductRelated_Duration": 60,
    "SpecialDay": 0.2,
    "Month": "Feb",
    "OperatingSystems": 2,
    "Browser": 2,
    "Region": 1,
    "TrafficType": 1,
    "VisitorType": "Returning_Visitor",
    "Weekend": 1,
}


def normalize_feature_value(feature: str, raw_value: str):
    if feature in {"Month", "VisitorType"}:
        return raw_value or ("Feb" if feature == "Month" else "Returning_Visitor")

    if feature == "Weekend":
        return 1 if str(raw_value).lower() in {"1", "true", "yes", "on"} else 0

    if raw_value == "":
        return 0

    return float(raw_value)


def build_prediction_payload(form_data: dict):
    values = {
        feature: normalize_feature_value(feature, form_data.get(feature, ""))
        for feature in features
    }
    frame = pd.DataFrame([values], columns=features)
    probability = model.predict_proba(frame)[0, 1]
    prediction = bool(probability >= threshold)
    return values, prediction, float(probability)


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    context = {
        "title": "Sales Conversion Dashboard",
        "features": features,
        "threshold": threshold,
        "months": MONTHS,
        "visitor_types": VISITOR_TYPES,
        "selected_values": DEFAULT_VALUES,
        "prediction": None,
        "probability": None,
        "message": "Enter visitor details to see whether this lead is likely to convert.",
    }
    return templates.TemplateResponse(request=request, name="index.html", context=context)


@app.post("/dashboard", response_class=HTMLResponse)
async def dashboard_submit(request: Request):
    form_data = await request.form()
    selected_values, prediction, probability = build_prediction_payload(dict(form_data))

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Sales Conversion Dashboard",
            "features": features,
            "threshold": threshold,
            "months": MONTHS,
            "visitor_types": VISITOR_TYPES,
            "selected_values": selected_values,
            "prediction": prediction,
            "probability": probability,
            "message": "Prediction generated successfully.",
        },
    )


@app.get("/")
def home():
    return {
        "message": "Sales Conversion Prediction API is running!",
        "model_loaded": True,
        "threshold": threshold,
        "number_of_features": len(features),
    }


@app.get("/model-info")
def model_info():
    return {
        "model_name": "Sales Conversion Random Forest",
        "threshold": threshold,
        "required_features": features,
    }
