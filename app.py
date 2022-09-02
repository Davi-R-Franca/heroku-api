from fastapi import FastAPI
from database import conn
from fastapi.middleware.cors import CORSMiddleware

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
async def cria_usuario(user):
    idt = conn.local.user.insert_one(user).inserted_id
    usuario = conn.local.user.find_one({"_id":idt})
    return usuario