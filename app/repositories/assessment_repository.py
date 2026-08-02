from sqlalchemy.orm import Session

from app.models.assessment import Assessment


def create_assessment(
    db: Session,
    assessment_data: dict
):
    assessment = Assessment(
        **assessment_data
    )

    db.add(assessment)
    db.commit()
    db.refresh(assessment)

    return assessment



def get_assessment_by_id(
    db: Session,
    assessment_id: int
):
    return (
        db.query(Assessment)
        .filter(
            Assessment.id == assessment_id
        )
        .first()
    )



def get_user_assessments(
    db: Session,
    user_id: int
):
    return (
        db.query(Assessment)
        .filter(
            Assessment.user_id == user_id
        )
        .all()
    )



def get_all_assessments(
    db: Session
):
    return db.query(Assessment).all()



def delete_assessment(
    db: Session,
    assessment_id: int
):
    assessment = get_assessment_by_id(
        db,
        assessment_id
    )

    if not assessment:
        return None

    db.delete(assessment)
    db.commit()

    return assessment