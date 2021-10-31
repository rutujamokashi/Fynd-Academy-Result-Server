from fastapi import FastAPI, File

from fastapi.responses import HTMLResponse

from route.user import user
# for generating otp
import math, random

app = FastAPI()

app.include_router(user)


@app.get("/{otp:str}")
def gerOTP():
    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqstuvwxyz"
    OTP = ""
    length = len(digit)
    for i in range(6):
        OTP += digit[math.floor(random.random()*length)]
    return {OTP}
    gerOTP()

