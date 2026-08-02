from sqlalchemy.orm import Session
from app.repositories.user_repository import (
    get_user_by_email,
    create_user,
)
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
)
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

# =========================
# Register User
# =========================
def register_user(
    db: Session,
    user: RegisterRequest,
):
    """
    Register user baru.
    """

    print("\n========== REGISTER ==========")
    print("Full Name :", user.full_name)
    print("Email     :", user.email)
    print("Password  :", user.password)

    existing_user = get_user_by_email(
        db,
        user.email,
    )

    print("Existing User :", existing_user)

    if existing_user:
        print("❌ Email sudah terdaftar")
        raise Exception(
            "Email already registered"
        )

    hashed_password = hash_password(
        user.password
    )

    print("Hashed Password :", hashed_password)

    new_user = create_user(
        db,
        {
            "full_name": user.full_name,
            "email": user.email,
            "password": hashed_password,
        },
    )

    print("✅ User berhasil dibuat")
    print("ID    :", new_user.id)
    print("Email :", new_user.email)
    print("==============================\n")

    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "full_name": new_user.full_name,
            "email": new_user.email,
        },
    }


# =========================
# Login User
# =========================
def login_user(
    db: Session,
    user: LoginRequest,
):
    """
    Login user dan generate JWT token.
    """

    print("\n========== LOGIN ==========")
    print("Input Email    :", user.email)
    print("Input Password :", user.password)

    db_user = get_user_by_email(
        db,
        user.email,
    )

    print("DB User :", db_user)

    if not db_user:
        print("❌ User tidak ditemukan")
        raise Exception(
            "Invalid email or password"
        )

    print("DB ID       :", db_user.id)
    print("DB Email    :", db_user.email)
    print("DB Password :", db_user.password)

    password_valid = verify_password(
        user.password,
        db_user.password,
    )

    print("Password Valid :", password_valid)

    if not password_valid:
        print("❌ Password tidak cocok")
        raise Exception(
            "Invalid email or password"
        )

    print("✅ Password cocok")

    access_token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email,
        }
    )

    print("JWT Token :", access_token)
    print("========== LOGIN SUCCESS ==========\n")

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "full_name": db_user.full_name,
            "email": db_user.email,
        },
    }