from fastapi import FastAPI
from typing import List, Optional 
from models import User, Gender, Role 
from uuid import UUID, uuid4


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Juanita", 
        middle_name="H",
        last_name="Perez",
        gender=Gender.female,
        roles=[Role.student]
    ),
       
    User(
        id=uuid4(), 
        first_name="Rodolfo", 
        middle_name="J",
        last_name="Vargas",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;
