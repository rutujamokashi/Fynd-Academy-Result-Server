from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/fynd_result")
meta = MetaData()
con = engine.connect()
