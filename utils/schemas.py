from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class UserBase(BaseModel):
    """Base model for user data."""
    name: str
    email: EmailStr


class UserCreate(UserBase):
    """Model for creating a new user."""
    password: str


class User(UserBase):
    """Model for retrieving user data."""
    id: int

    class Config:
        orm_mode = True


class BookDetailBase(BaseModel):
    """Base model for book details."""
    number_pages: int
    publisher: str
    language: str


class BookDetailCreate(BookDetailBase):
    """Model for creating book details."""
    pass


class BookDetail(BookDetailBase):
    """Model for retrieving book details."""
    id: int
    book_id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    """Base model for book data."""
    title: str
    isbn: str
    published_date: Optional[date]
    genre: str


class BookCreate(BookBase):
    """Model for creating a new book."""
    details: Optional[BookDetailCreate]


class Book(BookBase):
    """Model for retrieving book data."""
    id: int
    details: Optional[BookDetail]

    class Config:
        orm_mode = True


class BorrowedBookBase(BaseModel):
    """Base model for borrowed book data."""
    user_id: int
    book_id: int


class BorrowedBookCreate(BorrowedBookBase):
    """Model for creating a new borrowed book."""
    pass


class BorrowedBook(BorrowedBookBase):
    """Model for retrieving borrowed book data."""
    id: int
    borrow_date: date
    return_date: Optional[date]

    class Config:
        orm_mode = True
