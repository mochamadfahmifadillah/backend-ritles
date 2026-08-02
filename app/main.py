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
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
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