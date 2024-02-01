from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """Model representing users."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    membership_date = Column(Date, nullable=False)
    borrowed_books = relationship('BorrowedBook', back_populates='user')


class Book(Base):
    """Model representing books."""
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    published_date = Column(Date, nullable=False)
    genre = Column(String(50), nullable=False)
    details = relationship('BookDetail', back_populates='book', uselist=False)


class BookDetail(Base):
    """Model representing book details."""
    __tablename__ = 'book_details'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'),
                     unique=True, nullable=False)
    number_pages = Column(Integer, nullable=True)
    publisher = Column(String(50), nullable=True)
    language = Column(String(20), nullable=True)
    book = relationship('Book', back_populates='details')


class BorrowedBook(Base):
    """Model representing borrowed books."""
    __tablename__ = 'borrowed_books'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    user = relationship('User', back_populates='borrowed_books')
