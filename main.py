from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles


class AgeData(BaseModel):
    age: int

class AgeRes(BaseModel):
    isAdult: bool

api_app = FastAPI(title="api app")

def isAdult(age):
    if age >= 18:
        return True
    else:
        return False

@api_app.post("/age", response_model=AgeRes)
async def post_age(ageData: AgeData):
    return {"isAdult": isAdult(ageData.age)}


app = FastAPI(title="main app")
app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="public",html = True), name="public")