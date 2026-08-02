from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import get_current_user

from app.schemas.assessment import AssessmentCreate

from app.services.prediction_service import predict_fatigue


router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)


@router.post("/predict")
def predict(
    assessment: AssessmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    prediction = predict_fatigue(
        db=db,
        assessment=assessment,
        user_id=current_user.id,
    )

    return {
        "score": prediction.fatigue_score,
        "risk_level": prediction.risk_level,
        "model_version": prediction.model_version,
    }