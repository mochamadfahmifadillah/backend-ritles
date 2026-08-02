from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
import app.models

from app.routers import (
    auth,
    users,
    assessment,
    dashboard,
    recommendation,
    health,
)

app = FastAPI(
    title="Ritles API",
    description="Smart Mental Fatigue Detection API",
    version="1.0.0",
)

# =========================
# CORS
# =========================
origins = [
    "http://localhost:5173",
    "https://ritles-web-apps-5gi8.vercel.app/",  # ganti nanti dengan URL frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Database
# =========================
Base.metadata.create_all(bind=engine)

# =========================
# Routes
# =========================
@app.get("/", tags=["General"])
def root():
    return {
        "message": "Welcome to Ritles API",
        "version": "1.0.0",
        "status": "healthy",
    }


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(assessment.router)
app.include_router(dashboard.router)
app.include_router(recommendation.router)
app.include_router(health.router)