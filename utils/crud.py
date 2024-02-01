from sqlalchemy.orm import Session
from datetime import date

from . import models, schemas


#CRUD FOR USER

def read_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def read_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def read_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password
    db_user = models.User(name=user.name, email=user.email,
                          password=hashed_password,  membershipDate=date.today())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#For book

def create_book(db: Session, book: schemas.BookCreate):
    if book.details is not None:
        db_details = models.BookDetail(number_pages=book.details.number_pages, publisher=book.details.publisher, language=book.details.language)
        db.add(db_details)
    book.details  = db_details
    db_book = models.Book(title=book.title, isbn=book.isbn,
                          published_date=book.published_date, genre=book.genre, details=book.details)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def read_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def read_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def read_book_by_isbn(db: Session, isbn: str):
    return db.query(models.Book).filter(models.Book.isbn == isbn).first()
