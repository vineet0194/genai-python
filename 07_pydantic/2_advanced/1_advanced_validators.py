from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name')     # runs for multiple fields
    def names_must_be_capitalize(cls, values):      # will run for all v in values
        if not values.istitle():
            raise ValueError("Names must be titlised")

class User(BaseModel):
    email: str

    @field_validator('email', mode="before")
    def normalize_email(cls, v):
        return v.lower().strip()
    
class Produce(BaseModel):
    price: str  # $4.44

    @field_validator("price", mode="before")
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
class DateRange(BaseModel):
    start_data: datetime
    end_date: datetime

    @model_validator(mode="after")
    def validate(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError("enddate must be after start date")
        return values