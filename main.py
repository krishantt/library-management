from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils import crud, models, schemas
from utils.database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users CRUD operations


@app.get('/users/', response_model=list[schemas.User])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_users(db, skip=skip, limit=limit)


@app.get('/users/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.read_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@app.post('/users/', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.read_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# Books CRUD operations


@app.get('/books/', response_model=list[schemas.Book])
def get_book_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_books(db, skip=skip, limit=limit)


@app.get('/books/{book_id}', response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.read_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return db_book


@app.post('/books/', response_model=schemas.Book)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.read_book_by_isbn(db, isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already registered")
    return crud.create_book(db=db, book=book)

# Book details operations


@app.get('/books/{book_id}/details', response_model=schemas.BookDetail)
def get_book_details(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.read_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return db_book.details


@app.put('/books/{book_id}/details', response_model=schemas.BookDetail)
def put_book_details(book_id: int, book_details: schemas.BookDetailCreate, db: Session = Depends(get_db)):
    db_book = crud.read_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail='Book not found')
    return crud.update_book_details(db=db, book_id=book_id, book_details=book_details)

# Borrowed books operations


@app.get('/borrowed-books/', response_model=list[schemas.BorrowedBook])
def get_borrowed_book_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_borrowed_books(db, skip=skip, limit=limit)


@app.post('/borrowed-books/', response_model=schemas.BorrowedBook)
def borrow_book(borrow_book: schemas.BorrowedBookCreate, db: Session = Depends(get_db)):
    return crud.borrow_book(db=db, borrow_book=borrow_book)


@app.put('/borrowed-books/{book_id}/return', response_model=schemas.BorrowedBook)
def return_borrowed_book(book_id: int, db: Session = Depends(get_db)):
    return crud.return_book(db=db, book_id=book_id)
