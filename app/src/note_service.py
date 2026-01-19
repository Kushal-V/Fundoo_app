from sqlalchemy.orm import Session
from models.note import Note
from schemas.note import NoteCreate, NoteUpdate


# CREATE
def create_note(db: Session, data: NoteCreate):
    note = Note(
        title=data.title,
        description=data.description,
        user_id=data.user_id
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


# READ ALL (user-wise)
def get_user_notes(db: Session, user_id: int):
    return db.query(Note).filter(
        Note.user_id == user_id,
        Note.is_deleted == False
    ).all()


# READ ONE
def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()


# UPDATE
def update_note(db: Session, note_id: int, data: NoteUpdate):
    note = get_note(db, note_id)
    if not note:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(note, key, value)

    db.commit()
    db.refresh(note)
    return note


# DELETE (soft delete)
def delete_note(db: Session, note_id: int):
    note = get_note(db, note_id)
    if not note:
        return None

    note.is_deleted = True
    db.commit()
    return note
