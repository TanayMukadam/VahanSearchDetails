from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from Models.models import CreateUser, UserLogin, Token
from Auth.auth import get_password_hashed, verify_hashed_password, create_access_token
from Database.database import Database
from fastapi.security import OAuth2PasswordRequestForm

userRouter = APIRouter()



@userRouter.post("/create_user")
async def create_user(user_details: CreateUser):
    if not user_details.username or not user_details.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Please Enter Username or Password")
    db = Database()
    hash_password = get_password_hashed(user_details.password)
    user_created = db.create_user(user_details.username, hash_password)
    return user_created
    



@userRouter.post("/user_login", response_model=Token)
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    db = Database()
    
    user = db.get_user(form_data.username)
    
    if not user or not verify_hashed_password(form_data.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")
    
    if not user.get("is_active", False):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User account is not active")
    
    data = {"sub": user["username"]}
    access_token = create_access_token(data)
    
    return {"access_token": access_token, "token_type": "bearer"}
