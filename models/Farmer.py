from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from .Base import Base


class Farmer(Base):
    __tablename__ = 'Farmers'
    email = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    Phone  = Column(String)
    Address = Column(String)
    # District = relationship("District.id", back_populates="Farmers")


