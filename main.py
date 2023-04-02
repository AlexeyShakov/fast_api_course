from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


fake_users = [
    {"id": 1, "name": "Вова", "last_name": "Путин"},
    {"id": 2, "name": "Дима", "last_name": "Медведев"},
    {"id": 3, "name": "Виктор", "last_name": "Цой", "degree": [
        {"id": 1, "type_degree": "expert"}
    ]}
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "ruble", "side": "buy", "price": 1000, "amount": 5},
    {"id": 2, "user_id": 1, "currency": "ruble", "side": "sell", "price": 1500, "amount": 3}
]


class TypeDegree(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    type_degree: TypeDegree


class User(BaseModel):
    id: int
    name: str
    last_name: str
    degree: Optional[List[Degree]] = []

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float
    amount: float = Field(ge=0)


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    print("KEEEEEEK",[user for user in fake_users if user.get("id") == user_id])
    return [user for user in fake_users if user.get("id") == user_id]


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}

