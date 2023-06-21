from fastapi import FastAPI , Response , status , HTTPException,Depends
from pydantic import BaseModel
from fastapi.params import Body
import psycopg
from psycopg import connect, ClientCursor
import time 
from . import models,schemas,utils
from .database import engine,get_db
from sqlalchemy.orm import Session
from typing import List,Optional
from .routers import chat,user,auth
from .config import settings


models.Base.metadata.create_all(bind = engine)

app = FastAPI()


while True :
    try:
        conn = psycopg.connect(host="localhost", dbname= "indiefind" , user ="postgres", password = "0073232564",cursor_factory= ClientCursor)
        cursor = conn.cursor()
        print("Connected to DB")
        break
    except Exception as error:
        print("We could not connect to DB")
        print("Error:" ,error)
        time.sleep(2)

app.include_router(chat.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Hello World"}

