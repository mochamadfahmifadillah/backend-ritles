from sqlalchemy.orm import Session

from app.repositories.activity_repository import (
    create_activity,
    get_activity_by_id,
    get_user_activities,
    get_all_activities,
    delete_activity,
)

from app.schemas.activityNote import ActivityCreate


def create_activityNote(
    db: Session,
    activityNote: ActivityCreate,
    user_id: int,
):
    return create_activity(
        db,
        {
            "user_id": user_id,
            "title": activityNote.title,
            "note": activityNote.note,
        },
    )


def get_activityNote(
    db: Session,
    activityNote_id: int,
):
    activityNote = get_activity_by_id(
        db,
        activityNote_id,
    )

    if not activityNote:
        raise Exception("Activity Note not found")

    return activityNote


def get_user_activityNotes(
    db: Session,
    user_id: int,
):
    return get_user_activities(
        db,
        user_id,
    )


def get_all_activityNotes(
    db: Session,
):
    return get_all_activities(db)


def delete_activityNote(
    db: Session,
    activityNote_id: int,
):
    activityNote = delete_activity(
        db,
        activityNote_id,
    )

    if not activityNote:
        raise Exception("Activity Note not found")

    return {
        "message": "Activity Note deleted successfully"
    }