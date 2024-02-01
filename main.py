from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils import crud, models, schemas
from utils.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/users/', response_model=list[schemas.User])
def get_user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_users(db, skip=skip, limit=limit)


@app.get('/users/{user_id}', response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.read_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not Found')
    return db_user


@app.post('/users/',response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.read_user_by_email(db,email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get('/books/', response_model=list[schemas.Book])
def get_book_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.read_books(db, skip=skip, limit=limit)


@app.get('/books/{book_id}', response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.read_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail='Book not Found')
    return db_book


@app.post('/books/',response_model=schemas.Book)
async def create_book(book: schemas.BookCreate, db:Session=Depends(get_db)):
    db_book = crud.read_book_by_isbn(db,isbn=book.isbn)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already registered")
    return crud.create_book(db=db, book=book)


@app.get('/books/{book_id}/details', response_model=schemas.BookDetail)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.read_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail='Book not Found')
    return db_book.details
