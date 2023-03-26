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
    Farmer_id = Column(Integer, ForeignKey('Farmer.email'))
    Farmers = relationship("Farmer", back_populates="Store")

    def __init__(self, storeItem, quantity):
        self.storeItem = storeItem
        self.quantity = quantity

    def __repr__(self):
        return f"Store('{self.storeItem}', '{self.quantity}')"