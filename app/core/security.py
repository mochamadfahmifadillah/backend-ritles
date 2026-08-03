from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

def hash_password(password: str):
    print("\n========== HASH PASSWORD ==========")
    print("Input      :", repr(password))
    print("Type       :", type(password))
    print("Length     :", len(password))
    print("===================================")

    hashed = pwd_context.hash(password)

    print("Hash       :", hashed)
    print("Hash Length:", len(hashed))
    print("========== HASH SUCCESS ==========\n")

    return hashed


def verify_password(
    plain_password: str,
    hashed_password: str,
):
    print("\n========== VERIFY PASSWORD ==========")
    print("Plain Password :", repr(plain_password))
    print("Plain Length   :", len(plain_password))
    print("Hash Password  :", hashed_password)
    print("Hash Length    :", len(hashed_password))
    print("====================================")

    result = pwd_context.verify(
        plain_password,
        hashed_password,
    )

    print("Verify Result :", result)
    print("========== VERIFY END ==========\n")

    return result

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire,
        }
    )

    token = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    print("\n========== JWT ==========")
    print("Payload :", to_encode)
    print("Token   :", token)
    print("=========================\n")

    return token