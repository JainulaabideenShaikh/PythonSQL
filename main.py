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