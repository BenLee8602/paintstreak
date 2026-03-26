from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    username: str

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None

