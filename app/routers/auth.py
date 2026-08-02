from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import get_current_user

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)

from app.services.auth_service import (
    register_user,
    login_user,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# =========================
# Register
# =========================

@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db),
):

    try:

        return register_user(
            db,
            user,
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


# =========================
# Login
# =========================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    try:

        user = LoginRequest(
            email=form_data.username,
            password=form_data.password,
        )


        return login_user(
            db,
            user,
        )


    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


# =========================
# Current User
# =========================

@router.get("/me")
def current_user(
    user=Depends(get_current_user),
):

    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
    }


# =========================
# Logout
# =========================

@router.post("/logout")
def logout():

    return {
        "message": "Logout successful"
    }