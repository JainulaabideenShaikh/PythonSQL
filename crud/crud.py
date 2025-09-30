from sqlalchemy.orm import Session
from models import User,Book,Library,BookDetail 
import schemas.schemas as schemas, models.library as library_m

def create_library(db: Session, library: schemas.LibraryCreate):
    db_library = library_m.Library(name=library.name)
    db.add(db_library)
    db.commit()
    db.refresh(db_library)
    return db_library 

def create_book(db: Session, book: schemas.BookCreate):
    db_book = Book(title=book.title, library_id=book.library_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_book_detail(db: Session, book_id: int, detail: schemas.BookDetailCreate):
    db_detail = BookDetail(**detail.dict(), book_id=book_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def borrow_book(db: Session, user_id: int, book_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    book = db.query(Book).filter(Book.id == book_id).first()
    if user and book:
        user.books.append(book)
        db.commit()
    return user