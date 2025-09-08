from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
from Database.database import Database
from typing import Optional
from Models.models import SearchRequest
from Controllers.user import userRouter
from Controllers.result import resultRouter

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Or specify [""] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return "Welcome to VahanSearch Api"


app.include_router(userRouter, prefix="/auth")
app.include_router(resultRouter, prefix="/results")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)