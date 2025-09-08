from pydantic import BaseModel
from typing import Optional





class SearchRequest(BaseModel):
    reg_no: Optional[str] = None
    phone_no: Optional[str] = None
    
    
    
class CreateUser(BaseModel):
    username: str
    password: str

    
class UserLogin(BaseModel):
    username: str
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str