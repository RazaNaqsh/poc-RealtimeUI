# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class ResourceBase(BaseModel):
    name: str

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
