from fastapi import APIRouter
from db.database import con
from db.config import conf
from model.user import login, stuinfo, result, info
# for generating otp
import math, random
# for writing csv format file
import csv
from fpdf import FPDF
#emails
from fastapi import FastAPI,BackgroundTasks,UploadFile,File,Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail,MessageSchema,ConnectionConfig
from pydantic import BaseModel,EmailStr
from typing import List, Optional

from fastapi.responses import HTMLResponse
# instance of APIRouter()
from schema.user import EmailSchema

user = APIRouter()

# generating otp and send to mail and save in txt file
@user.post("/send_otp", status_code=201)# declare path operation u need to perform.. status code for response
async def send_otp():
    digit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    otp_m = ""
    length = len(digit)
    for i in range (6):
        otp_m += digit[math.floor(random.random()*length)]
        with open('file/otp.txt','w') as otp_file:
            for line in otp_m:
                otp_file.write(otp_m)
                break
        otp_file.close()
    otp_msg = MessageSchema(
        subject = "Genereated OTP using FastAPI",
        recipients = ["rutujamokashi2021@gmail.com"],  # List of recipients, as many as you can pass
        body = otp_m ,
        subtype = "string"
    )
    fm = FastMail(conf)
    await fm.send_message(otp_msg)
    return JSONResponse(status_code=200,content={'message':'Genereated OTP using FastAPI successfully mailed'})

# get  data from table
@user.get("/read",status_code=201)
async def read_data():
    info = con.execute(login.select()).fetchall()
    with open('file/info.csv','w')as csvfile:
        for data in info:
            csvfile.write(str(info))
            break
        field = ['lid', 'email']
        writer = csv.DictWriter(csvfile,fieldnames=field)# users from model.users
    csvfile.close()
    return info
# get data from table if lid = lid
@user.get("/{lid}")
async def read_data(lid:int):
    data = con.execute(login.select().where(login.c.lid == lid)).fetchall()
    with open('file/info.txt','w') as textfile:
        for info in data:
            textfile.write(str(data))
            textfile.close()
    return data
# get data from table if lid = lid
@user.get("/")
async def read_info(id:int):
    infodata = con.execute(info.select().where(info.c.id == id)).fetchall()
    # layout('P','L') #unit('cm','mm','in')  # format('A4','A3','default','letter','legel')
    pdf = FPDF('P','mm','Letter')# pdf vaiable/object of FPDF() class
    pdf.add_page()#for adding page
    pdf.set_font("Times",size=20)# format of pdf file
    with open('file/data.txt','w') as rfile:
        for i in infodata:
            rfile.write(str(infodata))# write data in txt file
            break
    pdf_file = open('file/data.txt','r')# open txt file in read mode
    #insert the data from txt file to pdf
    for i in pdf_file:
        # 200 = width 10 = height of pdf file
        pdf.cell(200 , 10 , txt=i , ln=1 , align='L')
        pdf.output("file/data.pdf")
    result_message = MessageSchema(
        subject="Genereated result in pdf format using FastAPI",
        recipients=["rutujamokashi2021@gmail.com"],  # List of recipients, as many as you can pass
        body=str(infodata),
        subtype="string"
    )
    fm = FastMail(conf)
    await fm.send_message(result_message)
    return JSONResponse(status_code=200, content={'message': 'Genereated result in pdf format using FastAPI successfully mailed'})


# sending pdf to gmail
@user.post('/send_mail')
async def send_mail(email: EmailSchema):
    result = "file/data.pdf"
    template='''
        <html>
            <body>
                 <p>Hi !!!
                 <br>Thanks for using fastapi mail, keep using it..!!!</p>
            </body>
        </html>
    '''

    message = MessageSchema(
        subject = "Result of Course",
        recipients = ["rutujamokashi2021@gmail.com"],  # List of recipients, as many as you can pass
        body = result ,
        subtype = "pdf"

    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200,content={'message':'pdf sent'})

@user.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
                             #properties: Properties):

     return {"filename": file.filename}

@user.post('/gen_otp_send-to-mail')
async def gen_otp(lid:int):
    digit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    otp_m = ""
    length = len(digit)
    for i in range (6):
        otp_m += digit[math.floor(random.random()*length)]
        with open('file/otp.txt','w') as otp_file:
            for line in otp_m:
                otp_file.write(otp_m)
                break
        otp_file.close()
    otp = con.execute(info.insert()).where(info.c.ot
    login.c.lid == lid)).fetchall()












