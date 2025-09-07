from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    customer = "customer"
    merchant = "merchant"


class UserCreate(BaseModel):
    username: str
    password: str
    role: Role


class UserLogin(BaseModel):
    username: str
    password: str


class TransactionCreate(BaseModel):
    merchant_id: int
    amount: float
