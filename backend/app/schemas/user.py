from pydantic import BaseModel, constr

Username = constr(pattern=r"^[0-9a-z._]+$")
Password = constr(pattern=r"^[ -~]+$")

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    username: Username

class UserUpdate(BaseModel):
    username: Username | None = None
    password: Password | None = None

class Token(BaseModel):
    token: str

