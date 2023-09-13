from fastapi import APIRouter, Depends, status, HTTPException
from database import get_db
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import schemas
import models

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(
        models.Seller.username == request.username).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid User")
    print(seller)
    print('hi')
    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Password")

    #generate JWT token
    return request