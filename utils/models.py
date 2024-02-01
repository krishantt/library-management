from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    membership_date = Column(Date, nullable=False)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    published_date = Column(Date, nullable=False)
    genre = Column(String(50), nullable=False)
    details = relationship('BookDetails', back_populates='book')

class BookDetails(Base):
    __tablename__ = 'book_details'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.BookID'), unique=True, nullable=False)
    number_pages = Column(Integer, nullable=False)
    publisher = Column(String(50), nullable=False)
    language = Column(String(20), nullable=False)
    book = relationship('Book', back_populates='details')

class BorrowedBooks(Base):
    __tablename__ = 'borrowed_books'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.UserID'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.BookID'), nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    user = relationship('User', back_populates='borrowed_books')