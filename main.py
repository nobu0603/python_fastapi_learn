from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def imdex():
    return {"message": "Hello World"}