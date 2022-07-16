from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    role: str


class ShowUser(BaseModel):
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True
