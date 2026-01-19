from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.dependency import get_db
from schemas.user import UserCreate, UserUpdate, UserResponse
from src.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter(prefix="/users", tags=["Users"])

# CREATE
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# READ ALL
@router.get("", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)


# READ ONE
@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# UPDATE
@router.put("/{user_id}", response_model=UserResponse)
def update_user_api(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = update_user(db, user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# DELETE
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
