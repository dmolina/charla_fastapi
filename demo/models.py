from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)

class Serie(Base):
    __tablename__ = "serie"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description  = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category')
