
from lib2to3.pgen2 import token
from multiprocessing import managers
from multiprocessing.dummy import Manager
from wsgiref.validate import validator
from xml.dom.expatbuilder import Rejecter
from fastapi import APIRouter, HTTPException, Query
from pymysql import Date
from sqlalchemy import DATE
from config.db import conn
from models.index import users,users2,users3,users4,users5,users6
from schemas.index import User
from schemas.user import Story, User_info
from schemas.user import user_Registration,Refer_user,CompletedStory
from config.db import SessionLocal
from config.db import Base,engine,MetaData
from typing import Union
#all create table comand
#Base.metadata.create_all(bind=engine)

#from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

user=APIRouter()


@user.get("/{id}")
async def search_admin(id:int):
    return conn.execute(users.select().where(users.c.id==id)).fetchall()

@user.post("/add_admin")
async def add_admin(user:User):
    conn.execute(users.insert().values(
        username=user.username,
        password=user.password,
    ))
    return conn.execute(users.select()).fetchall()

#updateadmin
@user.put("/update_admin/{id}")
async def update_admin(id:int,user:User):
    conn.execute(users.update().values(
        username=user.username, 
        password=user.password
    ).where(users.c.id==id))
    return conn.execute(users.select()).fetchall()

# user.delete("/")
# async def delete_data():
#     conn.execute(users.delete().where(users.c.id==id))
#     return conn.execute(users.select()).fetchall()


@user.get("/all_admin/")
async def all_admin():
    return conn.execute(users.select()).fetchall()

@user.post("/Admin_login/")
async def login_admin(user:User):
    data=conn.execute(users.select()).fetchall()
    for data in data:
        if data.username != user.username:
            return ("InvalidCredentialsException") 
        elif data.password != user.password:
            return ("InvalidCredentialsException")
        else:
             return{ 'status':'Successful login'}
        

# oauth2_schema=OAuth2PasswordBearer(tokenUrl="token") 
# @user.get("/items/")
# async def read_items(token:str =Depends(oauth2_schema)):
#     return{"token":token }  
#______-add user__________________________###

@user.post("/add_users")

async def add_users(user:User_info):
        conn.execute(users2.insert().values(
        First_name=user.First_name,
        Last_name=user.Last_name,
        Email_id=user.Email_id,
        Date_of_birth=user.Date_of_birth,
        Pen_name=user.Pen_name,
        Location=user.Location, 
        Password=user.Password,
        Conform_password=user.Conform_password,
        Refral_code=user.Refral_code,
        ))
        return{ "status":200 }

@user.post("/user_login")
async def user_login(user1:User):
    data=conn.execute(users2.select()).fetchall()
    for data in data:
        if data.Email_id!= user1.username:
            return ("InvalidCredentialsException") 
        elif data.Password != user1.password:
            return ("InvalidCredentialsException")
        else:
            return{ 'status':'Successful login'}


#take request from user 

@user.post("/user_request")
async def user_request(user2:user_Registration):
    try:
        conn.execute(users3.insert().values(
        First_name=user2.First_name,
        Last_name=user2.Last_name,
        Email_id=user2.Email_id,
        Status=user2.Status,
        Action=user2.Action,
        Roll=user2.Roll,
        isSuspend=user2.isSuspend

        ))  
        print("hgfd")
        return {"status":200,"message":"data added sucessfully..!!"}
    except Exception as ex:
        return ex


@user.get("/all_userRequest/")
async def all_userRequest():
    return conn.execute(users3.select()).fetchall()
#pendin api two api created active deactive and aprove and rejected
@user.get("/Admin_Aprove/")
async def all_userRequest():
    data= conn.execute(users3.select()).fetchall()
    for data in data:
        #q={"id":data.id,'Status': data.Status}
        if (data.Action != "active"):
            return  {'Status':"Rejected"}
        else: 
            return {'Status':"Sucessfulyy aproved"}
       
# add user story:  
@user.post("/add_user_story/")
async def add_users_story(user:Story):
        conn.execute(users4.insert().values(
        user_id =user.user_id,
        Approve_id=user.Approve_id,
        Reviwer_id=user.Reviwer_id,
        Title=user.Title,
        CreateDate=user.CreateDate,
        UpdateDate=user.UpdateDate,
        story_text=user.story_text,
        Author=user.Author,
        Issharable=user.Issharable,
        Iseditable=user.Iseditable,
        RejectReson=user.RejectReson,
        ))
        return {"status":200,"message":"data added sucessfully..!!"}

@user.post("/Refer_user/")
async def refer_user(user:Refer_user):
        conn.execute(users5.insert().values(
            First_user_ref_id=user.First_user_ref_id,
            Second_user_ref_id=user.Second_user_ref_id,
            Third_user_ref_id=user.Third_user_ref_id    
            ))
        return {"status":200,"message":"data added sucessfully..!!"}
        

@user.post("/Completstory/")
async def Completstory(use:CompletedStory):
        conn.execute(users6.insert().values(
        Title =use.Title,
        Status=use.Status,
        ImageUrl=use.ImageUrl,
        Story=use.Story,
        islike=use.islike,
        Dislike=use.Dislike,
        IsTrending =use.IsTrending,
        PublisheDate=use.PublisheDate,
        Tag=use.Tag,
        ))
        return {"status":200,"message":"data added sucessfully..!!"}



#show  get all authors:
@user.get("/All_authors/")
async def all_authors():
    data =conn.execute(users3.select()).fetchall()
    d=[]
    for data in data:
        da={"first_name":data.First_name,"last_name":data.Last_name,"Email_id":data.Email_id,"Action":data.Action}
        d.append(da)
    return {"status":200,"Authors":d} 

#published stories:
@user.get("/published_storis/")
async def all_published_storis():
        data=conn.execute(users6.select()).fetchall()
        da=[]
        for data in data:
            d={"title":data.Title,"Dislike":data.Dislike,"Like":data.islike,"Tag":data.Tag,"Status":data.Status,"Approved Date":data.PublisheDate}
            da.append(d)
        return {"status":200,"Authors":da}

@user.get("/to_Approve/")
async def to_Approve_story():
    data=conn.execute(users3,users6,users4.select()).fetchall()


