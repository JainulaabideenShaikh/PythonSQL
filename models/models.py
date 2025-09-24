from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.database import Base

# Many-to-Many Table
user_book_association = Table(
    'user_book',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True), 
    Column('book_id', ForeignKey('books.id'), primary_key=True)
)

class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    books = relationship("Book", back_populates="library")  # One-to-Many

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    library_id = Column(Integer, ForeignKey("libraries.id"))

    library = relationship("Library", back_populates="books")  # Many-to-One
    detail = relationship("BookDetail", uselist=False, back_populates="book")  # One-to-One
    users = relationship("User", secondary=user_book_association, back_populates="books")  # Many-to-Many

class BookDetail(Base):
    __tablename__ = 'book_details'
    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="detail")  # One-to-One

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    books = relationship("Book", secondary=user_book_association, back_populates="users")  # Many-to-Many
