from pydantic import BaseModel

class Login(BaseModel):
    lid = int,
    name = str


