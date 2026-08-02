from sqlalchemy.orm import Session

from app.repositories.assessment_repository import create_assessment

from app.repositories.prediction_repository import (
    create_prediction,
    get_prediction_by_id,
    get_user_predictions,
    get_all_predictions,
    delete_prediction,
)

from app.schemas.prediction import PredictionCreate


# ==========================================
# Simpan Prediction
# ==========================================

def create_prediction_result(
    db: Session,
    prediction: PredictionCreate,
    user_id: int,
):
    """
    Menyimpan hasil prediction.
    """

    return create_prediction(
        db,
        {
            "user_id": user_id,
            "fatigue_score": prediction.fatigue_score,
            "risk_level": prediction.risk_level,
            "model_version": prediction.model_version,
        },
    )


# ==========================================
# AI Prediction (Dummy)
# ==========================================

def predict_fatigue(
    db: Session,
    assessment,
    user_id: int,
):
    """
    Menghitung fatigue score,
    menyimpan assessment,
    lalu menyimpan prediction.
    """

    # ==========================
    # Dummy AI Score
    # ==========================

    fatigue_score = (
        (assessment.study_duration * 10)
        + (assessment.device_usage * 5)
        + (assessment.task_load * 10)
        - (assessment.sleep_duration * 8)
    )

    fatigue_score = max(
        0,
        min(100, fatigue_score),
    )

    # ==========================
    # Risk Level
    # ==========================

    if fatigue_score < 40:
        risk_level = "Rendah"

    elif fatigue_score < 70:
        risk_level = "Sedang"

    else:
        risk_level = "Tinggi"

    # ==========================
    # Simpan Assessment
    # ==========================

    create_assessment(
        db,
        {
            "user_id": user_id,
            "sleep_duration": assessment.sleep_duration,
            "study_duration": assessment.study_duration,
            "device_usage": assessment.device_usage,
            "task_load": assessment.task_load,
            "risk_level": risk_level,
        },
    )

    # ==========================
    # Simpan Prediction
    # ==========================

    prediction = create_prediction(
        db,
        {
            "user_id": user_id,
            "fatigue_score": fatigue_score,
            "risk_level": risk_level,
            "model_version": "v1.0",
        },
    )

    return prediction


# ==========================================
# Get Prediction by ID
# ==========================================

def get_prediction(
    db: Session,
    prediction_id: int,
):
    """
    Mengambil prediction berdasarkan ID.
    """

    prediction = get_prediction_by_id(
        db,
        prediction_id,
    )

    if not prediction:
        raise Exception("Prediction not found")

    return prediction


# ==========================================
# Get User Prediction History
# ==========================================

def get_user_prediction_history(
    db: Session,
    user_id: int,
):
    """
    Mengambil seluruh histori prediction user.
    """

    return get_user_predictions(
        db,
        user_id,
    )


# ==========================================
# Get All Predictions
# ==========================================

def get_all_prediction_results(
    db: Session,
):
    """
    Mengambil seluruh prediction.
    """

    return get_all_predictions(db)


# ==========================================
# Delete Prediction
# ==========================================

def delete_prediction_result(
    db: Session,
    prediction_id: int,
):
    """
    Menghapus prediction.
    """

    prediction = delete_prediction(
        db,
        prediction_id,
    )

    if not prediction:
        raise Exception("Prediction not found")

    return {
        "message": "Prediction deleted successfully"
    }