from pydantic import BaseModel


class RecommendationCreate(BaseModel):
    risk_level: str
    message: str


class RecommendationResponse(BaseModel):
    id: int
    user_id: int
    risk_level: str
    message: str

    class Config:
        from_attributes = True