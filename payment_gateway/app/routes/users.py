from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database
from passlib.hash import bcrypt
import jwt

router = APIRouter(prefix="/users", tags=["Users"])

SECRET_KEY = "testsecret"  # ⚡ for testing, replace in production

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Check if username exists
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_pw = bcrypt.hash(user.password)
    new_user = models.User(username=user.username, password=hashed_pw, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username, "role": new_user.role}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode({"sub": db_user.username}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}
