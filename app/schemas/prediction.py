from pydantic import BaseModel


class PredictionCreate(BaseModel):
    fatigue_score: float
    risk_level: str
    model_version: str


class PredictionResponse(BaseModel):
    id: int
    user_id: int
    fatigue_score: float
    risk_level: str
    model_version: str

    class Config:
        from_attributes = True