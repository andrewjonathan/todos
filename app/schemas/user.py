from pydantic import BaseModel

class UserAuth(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str

class UserRead(BaseModel):
    id: int