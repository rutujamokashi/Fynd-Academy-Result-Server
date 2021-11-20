from fastapi import FastAPI , File, UploadFile
from pydantic import BaseModel,EmailStr
from typing import List

class Login(BaseModel):
    lid = int,
    email = str

class Result(BaseModel):
    rid = int,
    course = str,
    grade = str,
    sid = int

class Stuinfo(BaseModel):
    sid = int,
    name = str,
    city = str,
    contact = str,
    lid = str

class Info(BaseModel):
    id = int,
    name = str,
    course = str,
    grade = str,
    otp = str

class EmailSchema(BaseModel):
   email: List[EmailStr]

class PydanticFile(BaseModel):
    file: UploadFile = File(...)



