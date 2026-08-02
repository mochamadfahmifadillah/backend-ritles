from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.profile_service import (
    get_profile,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{user_id}")
def profile(
    user_id: int,
    db: Session = Depends(get_db),
):
    try:
        return get_profile(
            db,
            user_id,
        )
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )