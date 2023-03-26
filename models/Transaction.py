from .Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship

class Transaction(Base):
    __tablename__ = 'Transaction'
    id = Column(Integer, primary_key=True,autoincrement=True)
    quantity = Column(Integer)
    created_time = Column(DateTime,server_default=func.now())
    updated_time = Column(DateTime,server_default=func.now(),onupdate=func.now())
    Buyer_id = Column(Integer, ForeignKey('Buyer.id'))
    Seller_id = Column(Integer, ForeignKey('Farmer.email'))
    Buyer = relationship("Buyer", back_populates="Transaction")
    Seller = relationship("Farmer", back_populates="Transaction")
    # Buyer = relationship("Buyer", back_populates="Transaction")
    # Seller = relationship("Farmer", back_populates="Transaction")

    def __init__(self, quantity, Buyer, Seller):
        self.quantity = quantity
        self.Buyer = Buyer
        self.Seller = Seller