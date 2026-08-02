from fastapi import APIRouter

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
)


@router.get("/{user_id}")
def recommendations(
    user_id: int,
):
    return {
        "user_id": user_id,
        "recommendations": [
            "Sleep earlier",
            "Reduce screen time",
            "Take a short break",
        ],
    }