from fastapi import FastAPI
# imoprting form user
from route.user import user


app = FastAPI()

app.include_router(user)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Fynd-Academy-Result-Server"}