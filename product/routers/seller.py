from fastapi import APIRouter, status, Response, HTTPException
from fastapi.params import Depends
from database import get_db
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models
import schemas

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

@router.post('/seller', response_model=schemas.DisplaySeller, tags=['Seller'])
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username,
        email=request.email,
        password = hashed_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller