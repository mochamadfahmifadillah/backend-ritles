from sqlalchemy.orm import Session

from app.models.assessment import Assessment
from app.schemas.assessment import AssessmentCreate


def predict_assessment(
    db: Session,
    user_id: int,
    assessment: AssessmentCreate,
):

    # sementara AI belum ada
    average = (
        assessment.sleep_duration +
        assessment.study_duration +
        assessment.device_usage +
        assessment.task_load
    ) / 4

    if average >= 7:
        risk = "Tinggi"
    elif average >= 4:
        risk = "Sedang"
    else:
        risk = "Rendah"

    new_assessment = Assessment(
        user_id=user_id,
        sleep_duration=assessment.sleep_duration,
        study_duration=assessment.study_duration,
        device_usage=assessment.device_usage,
        task_load=assessment.task_load,
        risk_level=risk,
    )

    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)

    return {
        "message": "Assessment berhasil",
        "assessment": new_assessment,
    }