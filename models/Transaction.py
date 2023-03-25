from .Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship

class Transaction(Base):
    __tablename__ = 'Transaction'
    id = Column(Integer, primary_key=True,autoincrement=True)
    quantity = Column(Integer)
    created_time = Column(DateTime,server_default=func.now())
    updated_time = Column(DateTime,server_default=func.now(),onupdate=func.now())
    Buyer = relationship("Buyer.id", back_populates="Transaction")
    Seller = relationship("Farmer.email", back_populates="Transaction")