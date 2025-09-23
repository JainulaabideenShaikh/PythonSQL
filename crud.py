from sqlalchemy.orm import Session
import models, schemas

def create_library(db: Session, library: schemas.LibraryCreate):
    db_library = models.Library(name=library.name)
    db.add(db_library)
    db.commit()
    db.refresh(db_library)
    return db_library 