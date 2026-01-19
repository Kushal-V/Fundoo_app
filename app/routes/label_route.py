from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.dependency import get_db
from schemas.label import LabelCreate, LabelResponse
from src.label_service import (
    create_label,
    add_label_to_note,
    remove_label_from_note
)

router = APIRouter(
    prefix="/labels",
    tags=["Labels"]
)

@router.post("", response_model=LabelResponse)
def create_label_api(data: LabelCreate, db: Session = Depends(get_db)):
    return create_label(db, data.name, data.user_id)


@router.post("/attach")
def attach_label(note_id: int, label_id: int, db: Session = Depends(get_db)):
    result = add_label_to_note(db, note_id, label_id)
    if not result:
        raise HTTPException(status_code=404, detail="Note or Label not found")
    return {"message": "Label attached to note"}


@router.post("/detach")
def detach_label(note_id: int, label_id: int, db: Session = Depends(get_db)):
    result = remove_label_from_note(db, note_id, label_id)
    if not result:
        raise HTTPException(status_code=404, detail="Note or Label not found")
    return {"message": "Label removed from note"}
