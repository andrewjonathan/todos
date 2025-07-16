from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoUpdate(BaseModel):
    id: int
    completed: bool

class TodoRead(BaseModel):
    id: int