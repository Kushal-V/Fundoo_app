from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.user import UserCreate, UserResponse
from src.user_service import create_user
from db.dependency import get_db

router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
