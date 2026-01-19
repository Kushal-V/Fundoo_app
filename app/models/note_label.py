from sqlalchemy import Table, Column, Integer, ForeignKey
from db.base import Base

note_labels = Table(
    "note_labels",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id", ondelete="CASCADE")),
    Column("label_id", Integer, ForeignKey("labels.id", ondelete="CASCADE"))
)
