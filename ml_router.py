from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import shutil
import os
from ml_model import PredictRequest
import ml_service

router = APIRouter()

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@router.post("/train")
async def train_model(
    file: UploadFile = File(...),
    features: str = Form(...),
    label: str = Form(...)
):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        feature_list = [f.strip() for f in features.split(",")]

        model_name = ml_service.train_model(file_path, feature_list, label)

        return {
            "status": "model trained",
            "model_name": model_name,
            "features": feature_list,
            "label": label
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/predict")
async def predict(request: PredictRequest):
    try:
        preds = ml_service.predict(request.model_name, request.data)
        return {"predictions": preds}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/models")
async def list_models():
    return ml_service.list_models()