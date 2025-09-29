from sqlalchemy import Table, Column, ForeignKey
from database.database import Base

user_book_association = Table(
    'user_book',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('book_id', ForeignKey('books.id'), primary_key=True)
    # ,schema="alembic"
)
# Many-to-Many Table