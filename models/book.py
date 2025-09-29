from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
# from association import user_book_association
from models.association import user_book_association

class Book(Base):
    __tablename__ = 'books'
    # __table_args__ = {"schema": "alembic"}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    library_id = Column(Integer, ForeignKey("libraries.id"))

    library = relationship("Library", back_populates="books") # Many-to-One
    detail = relationship("BookDetail", uselist=False, back_populates="book") # One-to-One
    users = relationship("User", secondary=user_book_association, back_populates="books")# Many-to-Many
