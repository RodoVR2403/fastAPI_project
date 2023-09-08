from fastapi import FastAPI, HTTPException
from typing import List, Optional 
from models import User, Gender, Role 
from uuid import UUID, uuid4



app = FastAPI()
#Here we are adding the DB part that will be showed in localhost:8000/api/v1/users
db: List[User] = [
    User(
        id=UUID("bc9a22e2-bbc0-4203-a559-65e2579985c3"), 
        first_name="Juanita", 
        middle_name="H",
        last_name="Perez",
        gender=Gender.female,
        roles=[Role.student]
    ),
       
    User(
        id=UUID("539671f2-6b98-47ca-9a54-9f0e47e073f1"), 
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

#With this we can register new users
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

#With this one, we can delete a user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/users")
async def change_user()