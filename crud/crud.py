from sqlalchemy.orm import Session
import models.models as models, schemas.schemas as schemas

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

def borrow_book(db: Session, user_id: int, book_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if user and book:
        user.books.append(book)
        db.commit()
    return user