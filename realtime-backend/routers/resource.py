# app/routers/resources.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils import schema
from ..api import resource
from ..database import db


router = APIRouter(prefix="/resources", tags=["resources"])

@router.get("/", response_model=list[schema.Resource])
def list_resources(db: Session = Depends(db.get_db)):
    return resource.get_resources(db)

@router.post("/", response_model=schema.Resource)
def create_resource(resource: schema.ResourceCreate, db: Session = Depends(db.get_db)):
    return resource.create_resource(db, resource)
