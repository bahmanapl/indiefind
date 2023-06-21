from fastapi import APIRouter, Depends, status , HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas,models,utils,oauth2
from ..database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .. import database

router = APIRouter(
    tags=["Authenticaiton"]
)

@router.post('/login',response_model= schemas.Token)
def login(user_credentials: schemas.UserLoginRespone, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credential")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credential")

    #create token 
    access_token = oauth2.create_access_token(data={"user_id" : user.id})

    # return token

    return { "access_token" : access_token , "token_type" : "bearer"}
