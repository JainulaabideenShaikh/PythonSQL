from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from models.association import user_book_association

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    books = relationship("Book", secondary=user_book_association, back_populates="users")
# Many-to-Many