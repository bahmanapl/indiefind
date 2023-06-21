#data base models
from .database import Base
from sqlalchemy import Column, Integer, String , Boolean, TEXT
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, nullable=False)
    userChat = Column(TEXT, nullable= False)
    openaiChat = Column(String, nullable= False)
    published = Column(Boolean,server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))




class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable= False, unique=True)
    password = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

