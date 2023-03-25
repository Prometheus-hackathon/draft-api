from .Base import Base
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import relationship

class District(Base):
    __tablename__ = 'District'
    id = Column(Integer, primary_key=True,autoincrement=True)
    districtName = Column(String)
    districtData = Column(String)
    created_time = Column(DateTime,server_default=func.now())
    updated_time = Column(DateTime,server_default=func.now(),onupdate=func.now())