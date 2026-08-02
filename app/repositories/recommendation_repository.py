from sqlalchemy.orm import Session
from app.models.recommendation import Recommendation


def create_recommendation(db: Session, recommendation_data: dict):
    recommendation = Recommendation(**recommendation_data)

    db.add(recommendation)
    db.commit()
    db.refresh(recommendation)

    return recommendation


def get_recommendation_by_id(db: Session, recommendation_id: int):
    return (
        db.query(Recommendation)
        .filter(Recommendation.id == recommendation_id)
        .first()
    )


def get_user_recommendations(db: Session, user_id: int):
    return (
        db.query(Recommendation)
        .filter(Recommendation.user_id == user_id)
        .all()
    )


def get_all_recommendations(db: Session):
    return db.query(Recommendation).all()


def delete_recommendation(db: Session, recommendation_id: int):
    recommendation = get_recommendation_by_id(db, recommendation_id)

    if not recommendation:
        return None

    db.delete(recommendation)
    db.commit()

    return recommendation