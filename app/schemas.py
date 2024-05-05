# app/schemas.py
import datetime

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    login: str
    password: str
    project_id: str
    env: str
    domain: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
    created_at: Optional[datetime.datetime]
    locktime: Optional[datetime.datetime]

    class Config:
        from_attributes = True
