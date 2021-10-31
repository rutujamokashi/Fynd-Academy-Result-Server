from sqlalchemy import Table ,Column
from sqlalchemy.sql.sqltypes import Integer,String
from db.database import meta
login = Table(
    'login',meta,
    Column("lid", Integer, primary_key=True),
    Column("email",String(100)),


)