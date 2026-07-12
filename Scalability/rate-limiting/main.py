from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import time

app = FastAPI(
    title="My FastAPI App",
    description="A simple FastAPI application",
    version="1.0.0",
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

in_memory_db = {}

# -----------------------------
# Rate Limiter Configuration
# -----------------------------
MAX_REQUESTS = 3
WINDOW_SECONDS = 120  # 2 minutes

# Structure:
# {
#   "127.0.0.1": {
#       "count": 3,
#       "window_start": 1720780000.0
#   }
# }
rate_limit_store = {}


def check_rate_limit(request: Request):
    client_ip = request.client.host
    now = time.time()

    if client_ip not in rate_limit_store:
        rate_limit_store[client_ip] = {
            "count": 1,
            "window_start": now,
        }
        return

    client = rate_limit_store[client_ip]

    # Has the current window expired?
    if now - client["window_start"] >= WINDOW_SECONDS:
        client["count"] = 1
        client["window_start"] = now
        return

    # Same window
    if client["count"] >= MAX_REQUESTS:
        retry_after = int(
            WINDOW_SECONDS - (now - client["window_start"])
        )

        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded. Retry after {retry_after} seconds.",
            headers={"Retry-After": str(retry_after)},
        )

    client["count"] += 1


@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI!"
    }


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item, request: Request):
    check_rate_limit(request)

    if item_id in in_memory_db:
        raise HTTPException(
            status_code=400,
            detail="Item already exists"
        )

    in_memory_db[item_id] = item.model_dump()

    return {
        "message": "Created",
        "item": in_memory_db[item_id]
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, request: Request):
    check_rate_limit(request)

    if item_id not in in_memory_db:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return in_memory_db[item_id]