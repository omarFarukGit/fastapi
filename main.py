from fastapi import FastAPI,HTTPException
from pymongo import collection
from config import collection

from schema import mongodbSchema

app=FastAPI()

@app.get('/{id}')
def root(id):
    return {"id":id}

    
@app.post('/user')
def create_user(user:mongodbSchema):
    try:
        user_dict = user.model_dump()
        collection.insert_one(user_dict)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  