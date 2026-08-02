from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    get_user_by_id,
)


def get_profile(
    db: Session,
    user_id: int,
):
    """
    Mengambil profil user berdasarkan ID.
    """

    user = get_user_by_id(
        db,
        user_id,
    )

    if not user:
        raise Exception("User not found")

    return user


def update_profile(
    db: Session,
    user_id: int,
    full_name: str,
):
    """
    Memperbarui profil user.
    """

    user = get_user_by_id(
        db,
        user_id,
    )

    if not user:
        raise Exception("User not found")

    user.full_name = full_name

    db.commit()
    db.refresh(user)

    return user


def delete_profile(
    db: Session,
    user_id: int,
):
    """
    Menghapus akun user.
    """

    user = get_user_by_id(
        db,
        user_id,
    )

    if not user:
        raise Exception("User not found")

    db.delete(user)
    db.commit()

    return {
        "message": "Profile deleted successfully"
    }