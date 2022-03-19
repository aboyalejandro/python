#Python
from os import path, stat
from typing import Optional
from enum import Enum
from uuid import UUID
from datetime import date
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File

app = FastAPI()

#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
    pass

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    ),
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_Id: UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    ),
    created_at: datetime = Field(default=datetime.now()),
    updated_at: Optional[datetime] = Field(default=None),
    by: User = Field(...)

#Operations

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}