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


    existing_user = get_user_by_email(
        db,
        user.email,
    )


    if existing_user:

        print("❌ Email sudah terdaftar")

        raise Exception(
            "Email already registered"
        )


    hashed_password = hash_password(
        user.password
    )


    new_user = create_user(
        db,
        {
            "full_name": user.full_name,
            "email": user.email,
            "password": hashed_password,
        },
    )


    print("User berhasil dibuat")
    print("User ID :", new_user.id)
    print("==============================\n")


    return {

        "message": "User registered successfully",

        "user": {

            "id": new_user.id,

            "full_name": new_user.full_name,

            "email": new_user.email,

        },

    }

def login_user(
    db: Session,
    user: LoginRequest,
):
    """
    Login user dan generate JWT token.
    """


    print("\n========== LOGIN ==========")

    print(
        "Email:",
        user.email
    )


    # Cari user berdasarkan email

    db_user = get_user_by_email(
        db,
        user.email,
    )


    if not db_user:

        print(
            "User tidak ditemukan"
        )

        raise Exception(
            "Invalid email or password"
        )

    try:

        password_valid = verify_password(
            user.password,
            db_user.password,
        )


    except Exception as e:

        print(
            "Password verify error:",
            str(e)
        )

        raise Exception(
            "Password verification failed"
        )



    if not password_valid:

        print(
            "Password salah"
        )

        raise Exception(
            "Invalid email or password"
        )



    print(
        "Password valid"
    )


    try:

        access_token = create_access_token(
            {
                "sub": str(db_user.id),
                "email": db_user.email,
            }
        )


    except Exception as e:

        print(
            "JWT Error:",
            str(e)
        )

        raise Exception(
            "Token generation failed"
        )



    print(
        "========== LOGIN SUCCESS =========="
    )



    return {

        "access_token": access_token,

        "token_type": "bearer",

        "user": {

            "id": db_user.id,

            "full_name": db_user.full_name,

            "email": db_user.email,

        },

    }