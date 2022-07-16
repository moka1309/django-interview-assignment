from pydantic import BaseModel
from typing import Union


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


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
