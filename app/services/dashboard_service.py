from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    get_user_by_id,
)

from app.repositories.assessment_repository import (
    get_user_assessments,
)

from app.repositories.activityNote_repository import (
    get_activity_notes_by_user,
)

from app.repositories.prediction_repository import (
    get_latest_prediction,
)

from app.repositories.recommendation_repository import (
    get_latest_recommendation,
)



def get_dashboard(
    db: Session,
    user_id: int,
):
    """
    Mengambil seluruh data dashboard milik user.
    """



    # ==========================
    # User
    # ==========================

    user = get_user_by_id(
        db,
        user_id,
    )


    if not user:
        raise Exception("User not found")





    # ==========================
    # Assessment
    # ==========================

    assessments = get_user_assessments(
        db,
        user_id,
    )





    # ==========================
    # Activity Notes
    # ==========================

    activity_notes = get_activity_notes_by_user(
        db,
        user_id,
    )





    # ==========================
    # Latest Prediction
    # ==========================

    latest_prediction = get_latest_prediction(
        db,
        user_id,
    )





    # ==========================
    # Latest Recommendation
    # ==========================

    latest_recommendation = get_latest_recommendation(
        db,
        user_id,
    )





    # ==========================
    # Response
    # ==========================

    return {


        "user": {

            "id": user.id,

            "full_name": user.full_name,

            "email": user.email,

        },



        "total_assessments": len(assessments),



        "total_activity_notes": len(activity_notes),





        "latest_prediction": (

            {

                "fatigue_score": latest_prediction.fatigue_score,

                "risk_level": latest_prediction.risk_level,

                "model_version": latest_prediction.model_version,

            }

            if latest_prediction

            else None

        ),





        "latest_recommendation": (

            {

                "risk_level": latest_recommendation.risk_level,

                "message": latest_recommendation.message,

            }

            if latest_recommendation

            else None

        ),





        "activity_notes": [

            {

                "id": note.id,

                "title": note.title,

                "note": note.note,

            }

            for note in activity_notes

        ],



    }