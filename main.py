from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@app.post("/libraries/", response_model=schemas.Library)
def create_library(library: schemas.LibraryCreate, db: Session = Depends(get_db)):
    return crud.create_library(db, library)

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.post("/books/{book_id}/detail/", response_model=schemas.BookDetail)
def add_book_detail(book_id: int, detail: schemas.BookDetailCreate, db: Session = Depends(get_db)):
    return crud.create_book_detail(db, book_id, detail)