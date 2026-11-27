from pydantic import BaseModel

class mongodbSchema(BaseModel):
    name: str
    email: str
    age: int