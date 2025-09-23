from sqlalchemy.orm import Session
import models, schemas

def create_library(db: Session, library: schemas.LibraryCreate):
    db_library = models.Library(name=library.name)
    db.add(db_library)
    db.commit()
    db.refresh(db_library)
    return db_library 

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, library_id=book.library_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_book_detail(db: Session, book_id: int, detail: schemas.BookDetailCreate):
    db_detail = models.BookDetail(**detail.dict(), book_id=book_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user