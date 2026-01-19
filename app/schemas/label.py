from pydantic import BaseModel

class LabelCreate(BaseModel):
    name: str
    user_id: int


class LabelResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True
