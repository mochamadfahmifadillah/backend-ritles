from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_assessments: int
    latest_risk: str | None
    average_score: float | None