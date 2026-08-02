from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import get_current_user

from app.schemas.activityNote import (
    ActivityNoteCreate,
    ActivityNoteResponse,
)

from app.services.activityNote_service import (
    create_activityNote,
    get_user_activityNotes,
)


router = APIRouter(
    prefix="/activity-note",
    tags=["Activity Note"],
)





@router.post(
    "",
    response_model=ActivityNoteResponse
)
def create(
    activity: ActivityNoteCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):

    return create_activityNote(
        db,
        activity,
        current_user.id,
    )






@router.get(
    "",
    response_model=list[ActivityNoteResponse]
)
def get_user_notes(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):

    return get_user_activityNotes(
        db,
        current_user.id,
    )