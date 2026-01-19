from sqlalchemy.orm import Session
from models.label import Label
from models.note import Note

# CREATE LABEL
def create_label(db: Session, name: str, user_id: int):
    label = Label(name=name, user_id=user_id)
    db.add(label)
    db.commit()
    db.refresh(label)
    return label


# ATTACH LABEL TO NOTE
def add_label_to_note(db: Session, note_id: int, label_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    label = db.query(Label).filter(Label.id == label_id).first()

    if not note or not label:
        return None

    note.labels.append(label)
    db.commit()
    return note


# REMOVE LABEL FROM NOTE
def remove_label_from_note(db: Session, note_id: int, label_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()
    label = db.query(Label).filter(Label.id == label_id).first()

    if not note or not label:
        return None

    note.labels.remove(label)
    db.commit()
    return note
