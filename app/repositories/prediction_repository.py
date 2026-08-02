from sqlalchemy.orm import Session

from app.models.prediction import Prediction


def create_prediction(
    db: Session,
    prediction_data: dict
):
    prediction = Prediction(
        **prediction_data
    )

    db.add(prediction)
    db.commit()
    db.refresh(prediction)

    return prediction



def get_prediction_by_id(
    db: Session,
    prediction_id: int
):
    return (
        db.query(Prediction)
        .filter(
            Prediction.id == prediction_id
        )
        .first()
    )



def get_user_predictions(
    db: Session,
    user_id: int
):
    return (
        db.query(Prediction)
        .filter(
            Prediction.user_id == user_id
        )
        .all()
    )



def get_all_predictions(
    db: Session
):
    return db.query(Prediction).all()



def delete_prediction(
    db: Session,
    prediction_id: int
):
    prediction = get_prediction_by_id(
        db,
        prediction_id
    )

    if not prediction:
        return None

    db.delete(prediction)
    db.commit()

    return prediction