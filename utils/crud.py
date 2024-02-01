from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy.orm.exc import NoResultFound

from . import models, schemas

# CRUD operations for User


def read_user(db: Session, user_id: int):
    """Retrieve a user by user_id."""
    return db.query(models.User).filter(models.User.id == user_id).first()


def read_user_by_email(db: Session, email: str):
    """Retrieve a user by email."""
    return db.query(models.User).filter(models.User.email == email).first()


def read_users(db: Session, skip: int = 0, limit: int = 100):
    """Retrieve a list of users with optional skip and limit."""
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user."""
    hashed_password = user.password
    db_user = models.User(name=user.name, email=user.email,
                          password=hashed_password, membership_date=date.today())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CRUD operations for Book


def create_book(db: Session, book: schemas.BookCreate):
    """Create a new book."""
    db_details = None
    if book.details:
        db_details = models.BookDetail(number_pages=book.details.number_pages,
                                       publisher=book.details.publisher, language=book.details.language)
        db.add(db_details)
    db_book = models.Book(title=book.title, isbn=book.isbn,
                          published_date=book.published_date, genre=book.genre, details=db_details)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    if db_details:
        db.refresh(db_details)
    return db_book


def read_book(db: Session, book_id: int):
    """Retrieve a book by book_id."""
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def read_books(db: Session, skip: int = 0, limit: int = 100):
    """Retrieve a list of books with optional skip and limit."""
    return db.query(models.Book).offset(skip).limit(limit).all()


def read_book_by_isbn(db: Session, isbn: str):
    """Retrieve a book by ISBN."""
    return db.query(models.Book).filter(models.Book.isbn == isbn).first()


def update_book_details(db: Session, book_id: int, book_details: schemas.BookDetailCreate):
    """Update or create book details."""
    existing_book = db.query(models.Book).filter(
        models.Book.id == book_id).first()

    try:
        db_details = db.query(models.BookDetail).filter(
            models.BookDetail.book_id == book_id).one()
        db_details.number_pages = book_details.number_pages
        db_details.publisher = book_details.publisher
        db_details.language = book_details.language
    except NoResultFound:
        db_details = models.BookDetail(number_pages=book_details.number_pages,
                                       publisher=book_details.publisher, language=book_details.language)
        db_details.book = existing_book

    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    return db_details

# CRUD operations for BorrowedBook


def read_borrowed_books(db: Session, skip: int = 0, limit: int = 100):
    """Retrieve a list of borrowed books with optional skip and limit."""
    return db.query(models.BorrowedBook).offset(skip).limit(limit).all()


def borrow_book(db: Session, borrow_book: schemas.BorrowedBookCreate):
    """Borrow a book."""
    db_borrow = models.BorrowedBook(
        user_id=borrow_book.user_id, book_id=borrow_book.user_id, borrow_date=date.today())
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow


def return_book(db: Session, book_id: int):
    """Return a borrowed book."""
    db_return = db.query(models.BorrowedBook).filter(
        models.BorrowedBook.book_id == book_id).one()
    db_return.return_date = date.today()
    db.add(db_return)
    db.commit()
    db.refresh(db_return)
    return db_return
