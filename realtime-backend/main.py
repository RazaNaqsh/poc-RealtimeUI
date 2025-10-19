# app/main.py
from fastapi import FastAPI
from .database.db import engine, Base
from .routers import resource

# Create tables (only for local dev; later we’ll use migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SSE Mini Project API")

# Include routes
app.include_router(resource.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}
