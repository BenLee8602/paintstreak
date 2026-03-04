from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")
async def root():
    return { "msg": "hello world!!!" }

