from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Library(Base):
    __tablename__ = 'libraries'
    # __table_args__ = {"schema": "alembic"}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    books = relationship("Book", back_populates="library") # One-to-Many