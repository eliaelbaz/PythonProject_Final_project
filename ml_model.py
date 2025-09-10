from pydantic import BaseModel
from typing import List, Dict, Any

class TrainRequest(BaseModel):
    csv_file: str
    features: List[str]
    label: str

class PredictRequest(BaseModel):
    model_name: str
    data: List[Dict[str, Any]]