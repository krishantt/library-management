from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class BookDetailBase(BaseModel):
    number_pages: int
    publisher: str
    language: str


class BookDetailCreate(BookDetailBase):
    pass


class BookDetail(BookDetailBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    isbn: str
    published_date: date
    genre: str
    

class BookCreate(BookBase):
    details: BookDetailBase | None = None



class Book(BookBase):
    id: int
    details: BookDetail | None = None

    class Config:
        orm_mode = True
