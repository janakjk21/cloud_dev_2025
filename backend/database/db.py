# database/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path to your database
DATABASE_URL = "sqlite:///./instance/appdatabase.db"

# Create engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

# Dependency: Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Mock user data (optional, for job credit checking)
_fake_user_db = {
    "username": "default_user",
    "credits": 10
}

def get_user():
    return _fake_user_db

def update_user_credits(username: str, new_credits: int):
    if username == _fake_user_db["username"]:
        _fake_user_db["credits"] = new_credits
    else:
        raise ValueError("User not found")
