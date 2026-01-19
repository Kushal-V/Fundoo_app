from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.dependency import get_db
from schemas.note import NoteCreate, NoteUpdate, NoteResponse
from src.note_service import (
    create_note,
    get_user_notes,
    update_note,
    delete_note,
    get_note
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note_api(data: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, data)


@router.get("/user/{user_id}", response_model=list[NoteResponse])
def get_notes_for_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_notes(db, user_id)


@router.get("/{note_id}", response_model=NoteResponse)
def get_note_api(note_id: int, db: Session = Depends(get_db)):
    note = get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=NoteResponse)
def update_note_api(
    note_id: int,
    data: NoteUpdate,
    db: Session = Depends(get_db)
):
    note = update_note(db, note_id, data)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note_api(note_id: int, db: Session = Depends(get_db)):
    note = delete_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
