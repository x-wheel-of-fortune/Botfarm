from fastapi import FastAPI
from .routes import router
from .dependencies import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from alembic.config import Config
from alembic import command


alembic_cfg = Config("alembic.ini")

SQLALCHEMY_DATABASE_URL = "postgresql://test:test@db/vk"

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

if __name__ == "__main__":
    command.upgrade(alembic_cfg, "head")