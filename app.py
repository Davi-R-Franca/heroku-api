from fastapi import FastAPI
from database import mydb, mycol
from user_model import User
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from user import userEntity, usersEntity

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://fastapiteste.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/usuario')
async def retorna_algo():
    return {"Olá":"Mundo"}

@app.post('/cria')
async def cria_usuario(user: User):
    new_user = dict(user)
    await mydb.mycol.insert_one(new_user).inserted_id
    #usuario = mydb.mycol.find_one({"_id":idt})
    return {"deu":"certo"}