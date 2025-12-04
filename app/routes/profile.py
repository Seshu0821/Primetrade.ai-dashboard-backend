from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.get("/me")
def get_profile(user=Depends(get_current_user)):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
