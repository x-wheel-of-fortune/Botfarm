from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import schemas, crud, models
from .dependencies import get_db

router = APIRouter()

class IdData(BaseModel):
    """Pydantic model for user ID data."""
    user_id: str

@router.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Endpoint to create a new user.

    Args:
        user (schemas.UserCreate): User data to be created.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        schemas.User: Created user data.
    """
    db_user = crud.get_user_by_login(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db=db, **user.dict())

@router.get("/get_users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    """Endpoint to get a list of all users.

    Args:
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        list[schemas.User]: List of users.
    """
    return crud.get_users(db=db)

@router.post("/acquirejock")
def acquire_jock(user_id: IdData, db: Session = Depends(get_db)):
    """Endpoint to acquire a lock for a user.

    Args:
        user_id (IdData): User ID data containing the user ID.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        dict: Success message.
    """
    db_user = crud.get_user_by_id(db, user_id.user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user.locktime:
        raise HTTPException(status_code=400, detail="User is already locked")

    crud.acquire_lock(db, user_id.user_id)
    return {"message": "Lock acquired successfully"}

@router.post("/releasejock")
def release_jock(user_id: IdData, db: Session = Depends(get_db)):
    """Endpoint to release a lock for a user.

    Args:
        user_id (IdData): User ID data containing the user ID.
        db (Session, optional): Database session. Defaults to Depends(get_db).

    Returns:
        dict: Success message.
    """
    db_user = crud.get_user_by_id(db, user_id.user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not db_user.locktime:
        raise HTTPException(status_code=400, detail="User is not locked")

    crud.release_lock(db, user_id.user_id)
    return {"message": "Lock released successfully"}
