from fastapi import APIRouter
from db.database import con
from model.user import login
user = APIRouter()

@user.get("/")
async def read_data():
    return con.execute(login.select()).fetchall()# users from model.users

@user.get("/{lid}")
async def read_data(lid:int):
    data = con.execute(login.select().where(login.c.lid == lid)).fetchall()
    return  data

