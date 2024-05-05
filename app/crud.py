from datetime import datetime

from sqlalchemy.orm import Session

from . import models


def create_user(db: Session, login: str, password: str, project_id: str,
                env: str, domain: str):
    """Create a new user in the database.

    Args:
        db (Session): Database session.
        login (str): User's login (email).
        password (str): User's password.
        project_id (str): ID of the project to which the user belongs.
        env (str): User's environment (prod, preprod, stage).
        domain (str): User's domain (canary, regular).

    Returns:
        models.UserModel: Created user object.
    """
    user = models.UserModel(login=login, password=password,
                            project_id=project_id, env=env, domain=domain)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    """Get all users from the database.

    Args:
        db (Session): Database session.

    Returns:
        list[models.UserModel]: List of users.
    """
    return db.query(models.UserModel).all()


def get_user_by_id(db: Session, user_id: str):
    """Get a user by ID from the database.

    Args:
        db (Session): Database session.
        user_id (str): ID of the user.

    Returns:
        models.UserModel: User object.
    """
    return db.query(models.UserModel).filter(
        models.UserModel.id == user_id).first()


def get_user_by_login(db: Session, login: str):
    """Get a user by login (email) from the database.

    Args:
        db (Session): Database session.
        login (str): User's login (email).

    Returns:
        models.UserModel: User object.
    """
    return db.query(models.UserModel).filter(
        models.UserModel.login == login).first()


def acquire_lock(db: Session, user_id: str):
    """Acquire a lock for a user.

    Args:
        db (Session): Database session.
        user_id (str): ID of the user to lock.

    Returns:
        models.UserModel: User object with lock applied.
    """
    user = get_user_by_id(db, user_id)
    if user.locktime:
        raise ValueError("User already locked")
    user.locktime = datetime.now()
    db.commit()
    return user


def release_lock(db: Session, user_id: str):
    """Release a lock for a user.

    Args:
        db (Session): Database session.
        user_id (str): ID of the user to unlock.

    Returns:
        models.UserModel: User object with lock removed.
    """
    user = get_user_by_id(db, user_id)
    if not user.locktime:
        raise ValueError("User is not locked")
    user.locktime = None
    db.commit()
    return user
