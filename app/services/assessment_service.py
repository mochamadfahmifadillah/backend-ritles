from sqlalchemy.orm import Session

from app.schemas.assessment import AssessmentCreate

from app.repositories.assessment_repository import (
    create_assessment,
)

from app.repositories.prediction_repository import (
    create_prediction,
)

from app.repositories.recommendation_repository import (
    create_recommendation,
)


def predict_assessment(
    db: Session,
    user_id: int,
    assessment: AssessmentCreate,
):

    # =========================
    # Hitung Fatigue Score
    # =========================

    score = (
        assessment.study_duration * 4 +
        assessment.device_usage * 3 +
        assessment.task_load * 3 -
        assessment.sleep_duration * 2
    )


    # Batasi nilai 0 - 100

    score = max(
        0,
        min(score, 100)
    )


    # =========================
    # Tentukan Risk Level
    # =========================

    if score >= 80:
        risk = "Tinggi"

    elif score >= 60:
        risk = "Sedang"

    else:
        risk = "Rendah"


    # =========================
    # Simpan Assessment
    # =========================

    assessment_data = {
        "user_id": user_id,
        "sleep_duration": assessment.sleep_duration,
        "study_duration": assessment.study_duration,
        "device_usage": assessment.device_usage,
        "task_load": assessment.task_load,
        "risk_level": risk,
    }


    new_assessment = create_assessment(
        db,
        assessment_data
    )


    # =========================
    # Simpan Prediction
    # =========================

    prediction_data = {
        "user_id": user_id,
        "fatigue_score": score,
        "risk_level": risk,
        "model_version": "Rule Based v1",
    }


    prediction = create_prediction(
        db,
        prediction_data
    )


    # =========================
    # Buat Recommendation
    # =========================

    if risk == "Tinggi":

        message = (
            "Segera kurangi aktivitas dan "
            "istirahat yang cukup."
        )

    elif risk == "Sedang":

        message = (
            "Atur waktu belajar dan istirahat "
            "agar lebih seimbang."
        )

    else:

        message = (
            "Pertahankan pola hidup sehat."
        )


    recommendation_data = {
        "user_id": user_id,
        "risk_level": risk,
        "message": message,
    }


    recommendation = create_recommendation(
        db,
        recommendation_data
    )


    # =========================
    # Response
    # =========================

    return {
        "message": "Assessment berhasil",
        "fatigue_score": score,
        "risk_level": risk,
        "recommendation": message,
        "model_version": prediction.model_version,
    }