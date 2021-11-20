from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer,String
from db.database import meta
login = Table(
    'login',meta,
    Column("lid", Integer, primary_key=True),
    Column("email",String(100)),
)
result = Table(
    'result',meta,
    Column('rid', Integer, primary_key=True),
    Column('course',String(50)),
    Column('grade',String(5)),
    Column('sid',Integer, ForeignKey("stuinfo.sid"))
)
stuinfo = Table(
    'stuinfo',meta,
    Column('sid',Integer, primary_key=True),
    Column('name',String(100)),
    Column('city',String(100)),
    Column('contact',String(20)),
    Column('lid',Integer,ForeignKey("login.lid"))
)
info = Table(
    'info',meta,
    Column('id',Integer, primary_key=True),
    Column('name',String(100)),
    Column('course',String(50)),
    Column('grade',String(5)),
    Column('otp',String(6))

)
