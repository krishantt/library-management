from sqlalchemy.orm import Session
from datetime import date

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password
    db_user = models.User(name=user.name, email=user.email,
                          password=hashed_password,  membershipDate=date.today())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
