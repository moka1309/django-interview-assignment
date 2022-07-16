from library.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(Enum('LIBRARIAN', 'MEMBER'), server_default="MEMBER")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String)
    status = Column(Enum('Borrowed', 'Available'), server_default="Available")
