from ast import Str
from datetime import date
from enum import Enum
from typing import Optional
from xmlrpc.client import Boolean
from pydantic import BaseModel,ValidationError,validator,Field
from pydantic.fields import ModelField
from typing import Union


from pymysql import Date
from sqlalchemy import TEXT, Text
# from fastapi import Request
# from starlette.responses import RedirectResponse
# user we pass all data nd datatype we have like pass information
class User(BaseModel):
    username:str
    password:str
 
class User_info(BaseModel):
    Email_id:str
    First_name:str =Field(...,exclusiveMinimum=1,exclusiveMaximum=30)
    Last_name:str 
    Date_of_birth:date
    Pen_name:str
    Location:Optional[str]=None
    Password:str
    Conform_password:str
    Refral_code:str

class Roll(str,Enum):
    ADMIN:"ADMIN"
    READER:"READER"
    WRITER:"WRITER"

class user_Registration(BaseModel):
    First_name:str =Field(...,exclusiveMinimum=1,exclusiveMaximum=30)
    Last_name:str 
    Email_id:str
    Status:str
    Action:str
    Roll:Roll
    isSuspend:Boolean

  
class Story(BaseModel):
    Title:str 
    CreateDate:str 
    UpdateDate:str
    story_text:str
    Reviwer_id:int
    Approve_id:int
    user_id:int
    Author:str
    Issharable:Boolean
    Iseditable:Boolean
    RejectReson:str



    
class Refer_user(BaseModel):
    First_user_ref_id:int
    Second_user_ref_id:int
    Third_user_ref_id:int

class CompletedStory(BaseModel):
    Title:str
    Status:str #published
    ImageUrl:str
    Story:str
    islike:bool
    Dislike:bool
    IsTrending:bool
    PublisheDate:Date
    Tag:str


class Config:
    orm_mode =True


# class NotAuthenticatedException(Exception):
#     pass
