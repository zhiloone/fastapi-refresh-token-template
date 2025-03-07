from contextlib import asynccontextmanager
from typing import Union

from fastapi import FastAPI

from src.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events"""
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
