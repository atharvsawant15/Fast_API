from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float

# Base class for models
class Base(DeclarativeBase):
    pass

# Product model
class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
