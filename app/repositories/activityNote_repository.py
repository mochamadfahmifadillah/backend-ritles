from sqlalchemy.orm import Session
from app.models.activityNote import ActivityNote


def create_activity_note(db: Session, activity_note_data: dict):
    activity_note = ActivityNote(**activity_note_data)

    db.add(activity_note)
    db.commit()
    db.refresh(activity_note)

    return activity_note


def get_activity_note_by_id(db: Session, activity_note_id: int):
    return (
        db.query(ActivityNote)
        .filter(ActivityNote.id == activity_note_id)
        .first()
    )


def get_activity_notes_by_user(db: Session, user_id: int):
    return (
        db.query(ActivityNote)
        .filter(ActivityNote.user_id == user_id)
        .all()
    )


def get_all_activity_notes(db: Session):
    return db.query(ActivityNote).all()


def delete_activity_note(db: Session, activity_note_id: int):
    activity_note = get_activity_note_by_id(db, activity_note_id)

    if not activity_note:
        return None

    db.delete(activity_note)
    db.commit()

    return activity_note