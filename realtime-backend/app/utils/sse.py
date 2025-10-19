# app/sse.py
import asyncio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import json

router = APIRouter()
queue = asyncio.Queue()  # global broadcast queue

async def event_generator():
    while True:
        data = await queue.get()  # wait for new resource
        yield f"data: {json.dumps(data)}\n\n"

@router.get("/events")
async def sse_endpoint():
    return StreamingResponse(event_generator(), media_type="text/event-stream")
