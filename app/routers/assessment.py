from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import get_current_user

from app.schemas.assessment import AssessmentCreate

from app.services.assessment_service import predict_assessment

from app.repositories.assessment_repository import (
    get_user_assessments,
)



router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)



# ==========================
# Predict Assessment
# ==========================

@router.post("/predict")
def predict(
    assessment: AssessmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    result = predict_assessment(
        db=db,
        assessment=assessment,
        user_id=current_user.id,
    )


    return result





# ==========================
# Assessment History
# ==========================

@router.get("/history")
def assessment_history(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    assessments = get_user_assessments(
        db,
        current_user.id,
    )


    return assessments