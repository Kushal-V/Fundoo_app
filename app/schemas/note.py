from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str | None = None
    description: str | None = None
    user_id: int


class NoteUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_archived: bool | None = None
    is_deleted: bool | None = None


class NoteResponse(BaseModel):
    id: int
    title: str | None
    description: str | None
    is_archived: bool
    is_deleted: bool
    user_id: int

    class Config:
        from_attributes = True
