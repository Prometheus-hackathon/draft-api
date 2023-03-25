from .Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship

class Store(Base):
    __tablename__ = 'Store'
    id = Column(Integer, primary_key=True,autoincrement=True)
    storeItem = Column(String)
    quantity = Column(Integer)
    created_time = Column(DateTime,server_default=func.now())
    updated_time = Column(DateTime,server_default=func.now(),onupdate=func.now())
    Farmers = relationship("Farmer.email", back_populates="Store")