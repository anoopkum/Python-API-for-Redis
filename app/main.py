from fastapi import FastAPI, File, UploadFile
from redis import Redis
from pydantic import BaseModel
import os
import yaml
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
redis_password = os.environ.get('REDIS_PASSWORD')
redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis_db = os.environ.get('REDIS_DB')
redis = Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

@app.post("/person")
async def create_person(file: UploadFile):
    contents = await file.read()
    data = yaml.safe_load(contents)
    print(data["first_name"])
    redis.hmset(data["first_name"], data)
    return {"message": "Person created successfully!"}

@app.get("/person/{first_name}")
def get_person(first_name: str):
    person_data = redis.hgetall(first_name)
    if not person_data:
        return {"message": "Person not found!"}
    return person_data