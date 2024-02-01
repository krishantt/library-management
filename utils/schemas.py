from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    name : str
    email :str

class UserCreate(UserBase):
    password : str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True