from fastapi import FastAPI
from .routes import router
from .dependencies import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

SQLALCHEMY_DATABASE_URL = "postgresql://test:test@localhost/vk"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Define the FastAPI app
app = FastAPI()

# Include routers
app.include_router(router)
