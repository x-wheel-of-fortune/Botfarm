# app/models.py

from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
import uuid
from datetime import datetime

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.now)
    login = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    project_id = Column(String, nullable=False)
    env = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    locktime = Column(DateTime, nullable=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


# Create session factory
SQLALCHEMY_DATABASE_URL = "postgresql://test:test@localhost/vk"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# CRUD operations

def create_user(db_session, login: str, password: str, project_id: str, env: str, domain: str):
    user = UserModel(login=login, password=password, project_id=project_id, env=env, domain=domain)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def get_user_by_login(db_session, login: str):
    return db_session.query(UserModel).filter(UserModel.login == login).first()


def get_users(db_session):
    return db_session.query(UserModel).all()


def update_user(db_session, user: UserModel, login: str, password: str, project_id: str, env: str, domain: str):
    user.login = login
    user.password = password
    user.project_id = project_id
    user.env = env
    user.domain = domain
    db_session.commit()
    db_session.refresh(user)
    return user


def delete_user(db_session, user: UserModel):
    db_session.delete(user)
    db_session.commit()
