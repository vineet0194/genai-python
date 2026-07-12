# Nested Models

from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    uid: int
    name: str
    address: Address        # nesting

address = {
    "street": "123 something",
    "city": "new delhi",
    "postal_code": "10001"
}

user_data = {
    "uid": 1,
    "name": "Vineet",
    "address" : address
}

try:
    user = User(**user_data)
    print("User created")
except Exception as e:
    print("Invalid data")