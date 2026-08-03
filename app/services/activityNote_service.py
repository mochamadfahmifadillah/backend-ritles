from sqlalchemy.orm import Session

from app.repositories.activityNote_repository import (
    create_activity_note,
    get_activity_note_by_id,
    get_activity_notes_by_user,
    get_all_activity_notes,
    delete_activity_note,
)

from app.schemas.activityNote import ActivityNoteCreate



def create_activityNote(
    db: Session,
    activityNote: ActivityNoteCreate,
    user_id: int,
):

    return create_activity_note(
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

    activityNote = get_activity_note_by_id(
        db,
        activityNote_id,
    )


    if not activityNote:
        raise Exception(
            "Activity Note not found"
        )


    return activityNote





def get_user_activityNotes(
    db: Session,
    user_id: int,
):

    return get_activity_notes_by_user(
        db,
        user_id,
    )



def get_all_activityNotes(
    db: Session,
):

    return get_all_activity_notes(db)



def delete_activityNote(
    db: Session,
    activityNote_id: int,
):

    activityNote = delete_activity_note(
        db,
        activityNote_id,
    )


    if not activityNote:
        raise Exception(
            "Activity Note not found"
        )


    return {
        "message":
        "Activity Note deleted successfully"
    }