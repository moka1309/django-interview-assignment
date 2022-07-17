from pydantic import BaseModel, validator
from typing import Union, Optional


class User(BaseModel):
    name: str
    email: str
    password: str
    role: Union[str, None] = None


class MemberUser(BaseModel):
    name: str
    email: str
    password: str


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


class Book(BaseModel):
    name: str
    author: str


class ShowBook(BaseModel):
    name: str
    author: str
    status: str

    class Config:
        orm_mode = True


class CurrentUser(BaseModel):
    email: str
    name: Union[str, None] = None
    role: Union[str, None] = None


class UserInDB(CurrentUser):
    hashed_password: str


class BookStatus(BaseModel):
    status: str
