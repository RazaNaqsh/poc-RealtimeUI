# app/routers/resources.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import schema
from ..api import resource
from ..database import db
from ..utils.sse import queue

router = APIRouter(prefix="/resources", tags=["resources"])

@router.get("/", response_model=list[schema.Resource])
def list_resources(db: Session = Depends(db.get_db)):
    return resource.get_resources(db)

@router.post("/", response_model=schema.Resource)
async def create_resource(data: schema.ResourceCreate, db: Session = Depends(db.get_db)):
    db_resource = resource.create_resource(db, data)
    await queue.put({"id": db_resource.id, "name": db_resource.name})  # await inside async route
    return db_resource

