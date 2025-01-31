import random

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from API import collection, user, wardrobe
from API.database import DB, get_database

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.include_router(collection.router, tags=["collection"])
app.include_router(wardrobe.router, tags=["wardrobe"])
app.include_router(user.router, tags=["user"])
app.add_middleware(SessionMiddleware, secret_key=random.random())
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    conn = get_database()
    database = DB(conn)
    database.initialize_db()
    uvicorn.run("main:app", port=8000, log_level="info")
