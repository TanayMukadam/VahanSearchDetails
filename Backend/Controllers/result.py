from fastapi import FastAPI, status, HTTPException, APIRouter, Depends
from Models.models import SearchRequest
from Database.database import Database
from Auth.auth import get_current_user

resultRouter = APIRouter()


@resultRouter.post("/get_results")
async def get_results(search_details: SearchRequest, current_user: dict = Depends(get_current_user)):
    if not search_details.reg_no and not search_details.phone_no:
        raise HTTPException(status_code=404, detail="Enter Registration Number or Phone Number")

    
    db = Database()  # create an instance
    results = db.get_result(search_details.reg_no, search_details.phone_no)  # call instance method
    
    return results
