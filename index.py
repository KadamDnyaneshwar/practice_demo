from fastapi import FastAPI

from schemas.user import User
from routes.index import user
app=FastAPI()
app.include_router(user)