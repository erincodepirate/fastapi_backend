from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50))
    description = Column(String(length=255))
    price = Column(Integer)
    seller_id = Column(Integer,ForeignKey('sellers.id'))
    seller = relationship("Seller",back_populates='products')

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50))
    email = Column(String(length=50))
    password = Column(String(length=60))
    products = relationship("Product",back_populates='seller')