# plan for backend

- This backend will first include CRUD APIs.
- First simple to just create the resources and save in DB.
- When the resource will be created and saved , then we want to implement SSE.


## Application Schema

Let the model and schema be basic for now

## What i learned from this

 - From the backend code point of, sse implementation was new to me.
 - This new concept of asyncio and event generator
 - creating an event endpoint for streaming responses


Then from docker point of view:
 - learned that by default the workdir in dockerfile is set to /app
 - so when we copy things inside .:/app , the codebase goes inside /app/app, thus have to run as app.main in the command
 - when we mount a volume, ./:/app, and my whole codebase was inside the backend folder, and when everything was at root destination, relative imports were causing issues
 - When i put all my codebase inside app folder then mounted volume, it worked.
