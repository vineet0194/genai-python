from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    uid: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    uid = 1,
    name = "Vineet",
    email = "vineet@ai.com",
    createdAt = datetime(2024, 3, 15, 14, 30, 20),
    address = Address(
        street="gali number 10",
        city="new delhi",
        postal_code="110071"
    ),
    is_active = False,
    tags = ["admin"]
)

# convert model to dictionary (Serialization)
res = user.model_dump()
print(res)

print()

# convert model to a json encoded string
json_res = user.model_dump_json()
print(json_res)