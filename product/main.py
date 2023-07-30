from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/product')
def add(request: schemas.Product):
    return request