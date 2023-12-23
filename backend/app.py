from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import user, auth
from database.config import engine, database, Base


app = FastAPI()
app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")

origins = [
    "http://localhost:5173",
]

methods = [
    "DELETE",
    "GET",
    "POST",
    "PUT",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"],
)


import asyncio


@app.on_event("startup")
async def startup():
    # Create a new event loop explicitly
    loop = asyncio.get_event_loop()

    # Use create_task to run async code in the background
    loop.create_task(create_tables())


async def create_tables():
    # Use the global database and engine objects
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# @app.on_event("shutdown")
# async def shutdown():
#     if database.is_connected:
#         await database.disconnect()
