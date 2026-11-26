from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

@app.get('/{id}')
def root(id):
    return {"id":id}

class User(BaseModel):
    name:str
    email:str
    age:int
    
@app.post('/')
def create(user:User):
    return {"success": True, "status_code": 201, "message": "user created successfully", "data": user.model_dump()}

class UpdateUser(BaseModel):
    name:str | None=None
    email:str | None=None
    age:int | None=None
    