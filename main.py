from fastapi import FastAPI

app = FastAPI()

@app.get("/countries/japan")
async def japan():
    return {"country_name": 'This is Japan!'}

@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}
