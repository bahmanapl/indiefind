from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional




class ChatBase(BaseModel):
    userChat:str 
    openaiChat:str
    published:bool = True


class ChatCreate(ChatBase):
    pass

class chatResponse(ChatBase):
    id:int
    created_at: datetime
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email:EmailStr 
    password:str

class UserCreateResponse(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UserLoginRespone(BaseModel):
    email :EmailStr
    password : str

class Token(BaseModel):
    access_token :str
    token_type:str

class TokenData(BaseModel):
    id : Optional[str] = None