from fastapi import APIRouter

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)


@router.post("/predict")
def predict():
    return {
        "message": "Prediction endpoint (AI belum diintegrasikan)"
    }