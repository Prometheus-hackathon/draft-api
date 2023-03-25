from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.Base import Base
from models.Farmer import Farmer
from models.Buyer import Buyer
from models.District import District
from models.Transaction import Transaction
from models.Store import Store

engine = create_engine('sqlite:///database.db',echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(Farmer(email="ajay#mai.com",first_name="ajay",last_name="kumar",Phone="1234567890",Address="ajay kumar"))
session.commit()