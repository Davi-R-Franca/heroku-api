from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def retorna_algo():
    return {"Olá":"Mundo"}