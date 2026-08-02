from pydantic import BaseModel


class AssessmentCreate(BaseModel):
    sleep_duration: float
    study_duration: float
    device_usage: float
    task_load: float


class AssessmentResponse(BaseModel):
    id: int
    user_id: int
    sleep_duration: float
    study_duration: float
    device_usage: float
    task_load: float
    risk_level: str

    class Config:
        from_attributes = True