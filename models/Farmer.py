from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from .Base import Base


class Farmer(Base):
    __tablename__ = 'Farmer'
    email = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    Phone  = Column(String)
    Address = Column(String)
    Password = Column(String)
    Transaction = relationship("Transaction", back_populates="Farmer")
    district_id = Column(Integer, ForeignKey('District.id'))

    district = relationship("District")

    def __init__(self, email, first_name, last_name, Phone, Address,Password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.Phone = Phone
        self.Address = Address
        self.Password = Password

    def __repr__(self):
        return f"Farmer('{self.email}', '{self.first_name}', '{self.last_name}', '{self.Phone}', '{self.Address}' , '{self.Password})"


