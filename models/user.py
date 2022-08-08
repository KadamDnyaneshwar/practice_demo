from datetime import date
import email
from email.policy import default
import enum
import string
from tokenize import String
from typing import Text
from xmlrpc.client import Boolean
from sqlalchemy import Date, Integer, Table,Column
from config.db import  meta
from sqlalchemy.sql.sqltypes import Integer,String,Boolean

users =Table(
    'admin',meta,
    Column('id',Integer,primary_key=True),
    Column('username',String(255)),
    Column('password',String(255))
)

users2 = Table(
    'user_info',meta,
    Column('id',Integer,primary_key=True),
    Column('Email_id',String(225)),
    Column('First_name',String(255)),
    Column('Last_name',String(255)), 
    Column('Date_of_birth',Date),
    Column('Pen_name',String(225)),
    Column('Location',String(255)),
    Column('Password',String(255)),
    Column('Conform_password',String(255)),
    Column('Refral_code',String(255))
)
users3 = Table(
    
    'User_Registration',meta,
    Column('id',Integer,primary_key=True),
    Column('First_name',String(255)),
    Column('Last_name',String(255)),
    Column('Email_id',String(225)),
    Column("Status",String(225)),
    Column("Action",String(225)),
    Column("Roll",String(225)),
    Column("isSuspend",Boolean)
)
#Roll :author , reader "Action":active /wi 

users4 =Table(
    "Story",meta,
    Column('id',Integer,primary_key=True),
    Column('user_id',Integer),
    Column('Approve_id',Integer),
    Column('Reviwer_id',Integer),
    Column('Title',String(255)),
    Column('CreateDate',Date),
    Column('UpdateDate',Date ),
    Column('story_text',String(250)),#64kb data hold up
    Column('Author',String(250)), #(ref for user)
    Column('Issharable',Boolean,default=True),
    Column('Iseditable',Boolean,default=True),
    Column('RejectReson',String(300)),
)


users5 =Table(
    "Refer_user",meta,
    Column('id',Integer,primary_key=True),
    Column('First_user_ref_id',Integer),
    Column('Second_user_ref_id',Integer),
    Column('Third_user_ref_id',Integer)
)

users6 =Table(
    "CompletedStory",meta,
    Column('id',Integer,primary_key=True),
    Column('Title',String(255)),
    Column('Status',String(255)), # published/unpublished
    Column('ImageUrl',String(255)),
    Column('Story',String(255)), #ref story table
    Column('islike',Boolean),# user like 
    Column('Dislike',Boolean),
    Column('IsTrending',Boolean),
    Column('PublisheDate',Date),
    Column('Tag',String(220)) 
    
    )