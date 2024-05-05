# app/crud.py

from sqlalchemy.orm import Session
from . import models
from datetime import datetime


def create_user(db: Session, login: str, password: str, project_id: str, env: str, domain: str):
    user = models.UserModel(login=login, password=password, project_id=project_id, env=env, domain=domain)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(models.UserModel).all()


def get_user_by_id(db: Session, user_id: str):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()


def get_user_by_login(db: Session, login: str):
    return db.query(models.UserModel).filter(models.UserModel.login == login).first()


def acquire_lock(db: Session, user_id: str):
    user = get_user_by_id(db, user_id)
    if user.locktime:
        raise ValueError("User already locked")
    user.locktime = datetime.now()
    db.commit()
    return user


def release_lock(db: Session, user_id: str):
    user = get_user_by_id(db, user_id)
    if not user.locktime:
        raise ValueError("User is not locked")
    user.locktime = None
    db.commit()
    return user
