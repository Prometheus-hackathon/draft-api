from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship
from .Base import Base

class Buyer(Base):
    __tablename__ = 'Buyer'
    id = Column(Integer, primary_key=True,autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    Phone  = Column(String)
    Address = Column(String)
    created_time = Column(DateTime,server_default=func.now())
    updated_time = Column(DateTime,server_default=func.now(),onupdate=func.now())
    purchase_id = Column(Integer, ForeignKey('Transaction.id'))
    purchases  = relationship("Transaction", back_populates="Buyer")

    def __init__(self, first_name, last_name, Phone, Address):
        self.first_name = first_name
        self.last_name = last_name
        self.Phone = Phone
        self.Address = Address

    def __repr__(self):
        return f"Buyer('{self.first_name}', '{self.last_name}', '{self.Phone}', '{self.Address}')"