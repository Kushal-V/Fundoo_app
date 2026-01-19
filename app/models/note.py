from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.base import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    description = Column(String, nullable=True)

    is_archived = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship("User", backref="notes")
