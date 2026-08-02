from pydantic import BaseModel, EmailStr


# =========================
# Register Schema
# =========================

class RegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str



# =========================
# Login Schema
# =========================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str



# =========================
# User Response
# =========================

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True



# =========================
# Token Response
# =========================

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse