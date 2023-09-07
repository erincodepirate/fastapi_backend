from sqlalchemy import Column, Integer, String
from database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    description = Column(String(length=255))
    price = Column(Integer)

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50))
    email = Column(String(length=50))
    password = Column(String(length=60))