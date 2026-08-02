from sqlalchemy.orm import Session

from app.repositories.prediction_repository import (
    create_prediction,
    get_prediction_by_id,
    get_user_predictions,
    get_all_predictions,
    delete_prediction,
)

from app.schemas.prediction import PredictionCreate


def create_prediction_result(
    db: Session,
    prediction: PredictionCreate,
    user_id: int,
):
    """
    Menyimpan hasil prediksi fatigue.
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


def get_all_prediction_results(
    db: Session,
):
    """
    Mengambil seluruh prediction.
    """

    return get_all_predictions(db)


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