from fastapi import FastAPI
from .database import conn

app = FastAPI()

@app.get('/')
async def retorna_algo():
    return {"Olá":"Mundo"}

@app.post('/cria')
async def cria_usuario(user):
    idt = conn.local.user.insert_one(user).inserted_id
    usuario = conn.local.user.find_one({"_id":idt})
    return usuario