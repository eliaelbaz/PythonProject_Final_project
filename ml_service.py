import os
import joblib
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression

MODELS_DIR = "models_store"

if not os.path.exists(MODELS_DIR):
    os.makedirs(MODELS_DIR)

def train_model(csv_file: str, features: list, label: str) -> str:
    df = pd.read_csv(csv_file)

    X = df[features]
    y = df[label]

    model = LinearRegression()
    model.fit(X, y)

    model_name = f"model_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pkl"
    model_path = os.path.join(MODELS_DIR, model_name)

    joblib.dump({
        "model": model,
        "features": features,
        "label": label,
        "trained_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }, model_path)

    return model_name

def predict(model_name: str, data: list):
    model_path = os.path.join(MODELS_DIR, model_name)
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model not found")

    obj = joblib.load(model_path)
    model = obj["model"]
    features = obj["features"]

    X_new = pd.DataFrame(data)[features]

    preds = model.predict(X_new)

    return preds.tolist()

def list_models():
    models = []
    for file in os.listdir(MODELS_DIR):
        if file.endswith(".pkl"):
            obj = joblib.load(os.path.join(MODELS_DIR, file))
            models.append({
                "name": file,
                "features": obj["features"],
                "label": obj["label"],
                "trained_at": obj["trained_at"]
            })
    return models