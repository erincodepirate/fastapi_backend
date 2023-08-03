from fastapi import FastAPI

import schemas
import models
from database import engine, SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.delete('/product/{id}')
def delete_product(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session = False)
    db.commit()
    return {'Product deleted'}

@app.put('/product/{id}')
def product(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        return {'Product does not exist'}
    product.update(request.dict())
    db.commit()
    return {'Product successfully updated'}

@app.get('/products')
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{id}')
def product(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    return product

@app.post('/product')
def add(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name,
        description =request.description,
        price=request.price,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request