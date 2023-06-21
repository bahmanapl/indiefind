from fastapi import FastAPI , Response , status , HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models,schemas,oauth2
from typing import List

router = APIRouter(
    prefix="/chats",
    tags = ["Chats"] # is used for better documentation
)

@router.get("/",response_model = List[schemas.chatResponse])
def get_chats(db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    chats = db.query(models.Chat).all()
    return chats


@router.get("/{id}",response_model= schemas.chatResponse)
def get_chat(id:int, db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    chat = db.query(models.Chat).filter(models.Chat.id == id).first()
    
    if not chat :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f"chat with the id {id} was not found")
    return chat


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.chatResponse)
def create_chats(chat:schemas.ChatCreate,db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    print(current_user)
    new_chat = models.Chat(**chat.dict())
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return new_chat

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chat(id:int,db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    chat = db.query(models.Chat).filter(models.Chat.id == id)

    if chat.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"chat with the id : {id} does not exist")
    chat.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model= schemas.chatResponse)
def update_chat(id:int,updated_chat:schemas.ChatCreate, db:Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    chat_query = db.query(models.Chat).filter(models.Chat.id == id)
    chat = chat_query.first()
    
    if chat == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail =f"chat with the id : {id} does not exist")
    chat_query.update(updated_chat.dict(),synchronize_session=False)
    db.commit()
    return chat_query.first()




