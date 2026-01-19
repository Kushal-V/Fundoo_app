from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from utils.password import hash_password

# CREATE
def create_user(db: Session, user: UserCreate):
    if db.query(User).filter(User.email == user.email).first():
        raise ValueError("User already exists")

    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# READ (ALL)
def get_all_users(db: Session):
    return db.query(User).all()


# READ (ONE)
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# UPDATE
def update_user(db: Session, user_id: int, data: UserUpdate):
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    if data.email:
        user.email = data.email
    if data.password:
        user.password = hash_password(data.password)

    db.commit()
    db.refresh(user)
    return user


# DELETE
def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
