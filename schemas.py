from pydantic import BaseModel
from typing import List, Optional

class BookDetailBase(BaseModel):
    isbn: str

class BookDetailCreate(BookDetailBase):
    pass

class BookDetail(BookDetailBase):
    id: int
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    library_id: int 

class Book(BookBase):
    id: int
    detail: Optional[BookDetail]
    class Config:
        orm_mode = True

class LibraryBase(BaseModel):
    name: str

class LibraryCreate(LibraryBase):
    pass

class Library(LibraryBase):
    id: int
    books: List[Book] = []
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    books: List[Book] = []
    class Config:
        orm_mode = True
