from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base

class Label(Base):
    __tablename__ = "labels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    notes = relationship(
        "Note",
        secondary="note_labels",
        back_populates="labels"
    )
