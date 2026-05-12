from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

#   Link model to database
Base = declarative_base()

#   ORM - map and define object to be used in database.
class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(String)
