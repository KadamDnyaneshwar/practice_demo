
import email
from mailjet_rest import Client
import os

from lib2to3.pgen2 import token
from multiprocessing import managers
from multiprocessing.dummy import Manager
from urllib import request
from wsgiref.validate import validator
from xml.dom.expatbuilder import Rejecter
from fastapi import APIRouter, HTTPException, Query
from pymysql import Date
from sqlalchemy import DATE
from config.db import conn
from models.index import users,users2,users3,users4,users5,users6,users7,users8
from schemas.index import User
from schemas.user import  Story, User_info,FeedBack,users_likes
from schemas.user import user_Registration,Refer_user,CompletedStory
from config.db import SessionLocal
from config.db import Base,engine,MetaData
from typing import Union
from typing import List
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import parse_obj_as,EmailStr, BaseModel
from dataclasses import dataclass

import smtplib as s
#from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
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
        id=user2.id,
        First_name=user2.First_name,
        Last_name=user2.Last_name,
        Email_id=user2.Email_id,
        Status=user2.Status,
        Action=user2.Action,
        Roll=user2.Roll,
        isSuspend=user2.isSuspend

        ))  
        print("hgfd ")
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
        SubmitedDate=user.SubmitedDate,
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
"======================================================================================"

@user.post("/send_mail/")
async def send_mail():
    api_key = 'a72d2140fe43bf95252424a746ddb776'
    api_secret = '5897bb4d9bf41e560fad7980a0677671'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
        {
        "From": {
            "Email": "dnyaneshwar.kadam@infeon.in",
            "Name": "dnyaneshwar"
        },
        "To": [
            {
            "Email": "dnyaneshwar.kadam@infeon.in",
            "Name": "swapnil"
            }
        ],
        "Subject": "Greetings from Mailjet.",
        "TextPart": "My first Mailjet email",
        "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
        "CustomID": "AppGettingStartedTest"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print( result.json())
    return{"message":"sucessfully send the email"}


    # ab=s.SMTP("smtp.gmail.com",587)
    # ab.starttls()
    # ab.login("skadam311@gmail.com","pass@123")
    # subject="sending mail"
    # body=" this is tutorial odf sending email using "
    # message="subject:{}/n/n{}".format(subject,body)

    # listofaddress=[]
    # ab.sendmail("skadam311@gmail.com",listofaddress,message)

    # print ("sucessfully")
    # return {"message":"sucessfully"}





# 	template = """
# 		<html>
# 		<body>
		

# <p>Hi !!!
# 		<br>Thanks for using fastapi mail, keep using it..!!!</p>


# 		</body>
# 		</html>
# 		"""

# 	message = MessageSchema(
# 		subject="Fastapi-Mail module",
# 		recipients=email.dict().get("email"), # List of recipients, as many as you can pass
# 		body=template,
# 		subtype="html"
# 		)

# 	fm = FastMail(conn)
# 	await fm.send_message(message)
# 	print(message)

# 	return JSONResponse(status_code=200, content={"message": "email has been sent"})


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
#total approve stories: Author name ,title, submited date,action
@user.get("/to_Approve/")
async def to_Approve_story():
    query ="""select user_Registration.first_name as author, story.Title as title,story.SubmitedDate
                from user_Registration,story where user_Registration.id=story.user_id"""    
    data=conn.execute(query).fetchall()
    return data

@user.get("/to_Rjected/")
async def to_Rjected_story():
    query ="""SELECT User_Registration.Action AS Action,
            completedstory.Title AS Title,completedstory.PublisheDate from User_Registration jOIN completedstory ON
            user_Registration.id=completedstory.id
                where user_Registration.Action ='deactive'"""
    data=conn.execute(query).fetchall()
    return data

#contactus and feedback
@user.post("/feedback/")
async def feedback(user:FeedBack):
    conn.execute(users7.insert().values(
        Email =user.Email,
        Name=user.Name,
        Subject=user.Subject,
        message =user.message,
        createdDate=user.createdDate,
        Status=user.Status))
    return {"status":200,"message":"data added sucessfully..!!"}

@user.post("/Show_feedback/")
async def Show_feedback():
    data=conn.execute(users7.select()).fetchall()
    return data

#likes 
@user.get("/showlikes/{id}")
async def show_likes():
    query="SELECT COUNT(islike) AS likes FROM completedstory where id='{}'"
    data=conn.execute(query).fetchone()
    print (data)
    return data

@user.get("/showdislikes/{id}")
async def show_likes():
    query="SELECT COUNT(Dislike)  As Dislike FROM completedstory where id='{}'"
    data=conn.execute(query).fetchone()
    print (data)
    return data

  
    
@user.get("/addlikes/{id}")
async def add_likes():

    query="update users_likes set islike ='"+islike+1+"' where user_id={}"   
    data=conn.execute(query)
    print(data)
    return {"status":200,"message":data }
      
    
@user.get("/disikes/{id}")
async def add_likes():

    query="update users_likes set islike ='"+dislike+1+"' where user_id={}"   
    data=conn.execute(query)
    print(data)
    return {"status":200,"message":data }
      
 
 

#action Api authors total details
@user.get("/Action/")
async def Action():
    data=conn.execute(users7.select()).fetchall()
    for data in data:
        return {"Name":data.Name,"Email":data.Email,"Subject":data.Subject,"message":data.message,"Date":data.createdDate}

#ui side api 
@user.get("/featured/")
async def featured():
    query="select * from story s join completedstory t1 on s.id=t1.id "
    data=conn.execute(query).fetchall()
    return data
      
@user.get("/popular/")
async def popular():
    query="SELECT * FROM completedstory join story on story.user_id=1"
    data=conn.execute(query).fetchall()
    return data

#storise and all storise same api
@user.get("/all_strosise/")
async def all_storise():
    query="SELECT * FROM completedstory "
    data=conn.execute(query).fetchall()
    return data    
    
@user.get("/recent_story/")
async def recent_storise():
    query="SELECT * from completedstory ORDER BY PublisheDate Desc"
    data=conn.execute(query).fetchall()
    return data  

@user.get("/status/")
async def status():
    pass




