# app/main.py
from fastapi import FastAPI
from .database.db import engine, Base
from .routers import resource
from .utils import sse

from fastapi.middleware.cors import CORSMiddleware

# Create tables (only for local dev; later we’ll use migrations)
Base.metadata.create_all(bind=engine)


app = FastAPI(title="SSE Mini Project API")

origins = [
    "http://localhost:3000",  # frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(resource.router)
app.include_router(sse.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}
