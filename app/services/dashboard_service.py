from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    get_user_by_id,
)

from app.repositories.assessment_repository import (
    get_user_assessments,
)

from app.repositories.prediction_repository import (
    get_user_predictions,
)

from app.repositories.activityNote_repository import (
    get_activity_notes_by_user,
)

from app.repositories.recommendation_repository import (
    get_user_recommendations,
)


def get_dashboard(
    db: Session,
    user_id: int,
):
    """
    Mengambil seluruh data dashboard milik user.
    """

    user = get_user_by_id(
        db,
        user_id,
    )

    if not user:
        raise Exception("User not found")


    assessments = get_user_assessments(
        db,
        user_id,
    )


    predictions = get_user_predictions(
        db,
        user_id,
    )


    recommendations = get_user_recommendations(
        db,
        user_id,
    )


    activity_notes = get_activity_notes_by_user(
        db,
        user_id,
    )


    latest_prediction = (
        predictions[-1]
        if predictions
        else None
    )


    latest_recommendation = (
        recommendations[-1]
        if recommendations
        else None
    )


    return {
        "user": user,
        "total_assessments": len(assessments),
        "total_activity_notes": len(activity_notes),
        "latest_prediction": latest_prediction,
        "latest_recommendation": latest_recommendation,
        "activity_notes": activity_notes,
    }