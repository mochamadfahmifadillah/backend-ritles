from pydantic import BaseModel


class ActivityNoteCreate(BaseModel):
    title: str
    note: str


class ActivityNoteResponse(BaseModel):
    id: int
    user_id: int
    title: str
    note: str

    class Config:
        from_attributes = True