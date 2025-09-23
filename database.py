from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
DATABASE_URL = f"postgresql://{user_name}:{password}@localhost:5432/dj14"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)