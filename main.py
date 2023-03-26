from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.Base import Base
from models.District import District
from models.Farmer import Farmer
from models.Buyer import Buyer
from models.Transaction import Transaction
from models.Store import Store
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL= os.getenv("DATABASE_URL") 
engine = create_engine(DATABASE_URL,echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get('/')
def index():
    return {'key': 'value'}

class USER(BaseModel):
    email:str
    password:str

@app.post('/farmer/auth')
def auth(body_part:USER):
    return {
        "email":body_part.email,
        "password":body_part.password
    }

@app.get('/farmer/auth')
def auth(*,email:Optional[str]=None,password:str,number:Optional[int]=None):
    if number is not None:
        user = session.query(Farmer).filter(Farmer.Phone==number,Farmer.Password==number).first()
        if user is not None:
            return {"data":"success"}
        else:
            return {"data":"user_not_found"}
    else: 
        if email is not None:
            user = session.query(Farmer).filter(Farmer.email==email,Farmer.Password==password).first()
            if user is not None:
                return {"data":"success"}
            else:
                return {"data":"user_not_found"}
        else:
            return {"data":"user_not_found"}
        
@app.get('/buyer/auth')
def auth(*,email:Optional[str]=None,password:str,number:Optional[int]=None):
    if number is not None:
        return {"number":number,"password":password}
    else: 
        if email is not None:
            return {"email":email,"password":password}
        else:
            return {"data":"miss matched"}

@app.post('/buyer/auth')
def auth(body_part:USER):
    return {
        "email":body_part.email,
        "password":body_part.password
    }






    


# session.add(Farmer(email="ajay#mai.com",first_name="ajay",last_name="kumar",Phone="1234567890",Address="ajay kumar"))
# session.commit()

