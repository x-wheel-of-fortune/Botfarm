# app/dependencies.py

from sqlalchemy.orm import Session
from .models import SessionLocal, engine

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
