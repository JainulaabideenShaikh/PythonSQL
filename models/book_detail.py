from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class BookDetail(Base):
    __tablename__ = 'book_details'
    # __table_args__ = {"schema": "alembic"}

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="detail") # One-to-One
