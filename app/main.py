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
    activityNote,
    health,
)



app = FastAPI(

    title="Ritles API",

    description="Smart Mental Fatigue Detection API",

    version="1.0.0",

)

origins = [

    "http://localhost:5173",

    "https://ritles-web-apps-16oy.vercel.app",
    "https://ritles-web-apps-news.vercel.app",
    "https://ritles-web-apps-news-git-main-fahmis-projects-58b8f18c.vercel.app",
    "https://ritlesweb.vercel.app",
    "https://ritleswebs.vercel.app",

]



app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

Base.metadata.create_all(
    bind=engine
)

@app.get(
    "/",
    tags=["General"]
)
def root():

    return {

        "message": "Welcome to Ritles API",

        "version": "1.0.0",

        "status": "healthy",

    }

app.include_router(
    auth.router
)


app.include_router(
    users.router
)


app.include_router(
    assessment.router
)


app.include_router(
    dashboard.router
)


app.include_router(
    recommendation.router
)


app.include_router(
    activityNote.router
)


app.include_router(
    health.router
)