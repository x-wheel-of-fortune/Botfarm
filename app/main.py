import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from .routes import router

load_dotenv()
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URL'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
