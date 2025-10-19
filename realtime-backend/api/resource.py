# app/crud.py
from sqlalchemy.orm import Session
from ..utils import models, schema, sse
import asyncio
from ..utils.sse import queue


def get_resources(db: Session):
    return db.query(models.Resource).order_by(models.Resource.id.desc()).all()

def create_resource(db: Session, resource: schema.ResourceCreate):
    db_resource = models.Resource(name=resource.name)
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    asyncio.create_task(queue.put({"id": db_resource.id, "name": db_resource.name}))
    return db_resource
