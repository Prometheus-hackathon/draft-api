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
    purchases  = relationship("Transaction.id", back_populates="Buyer")