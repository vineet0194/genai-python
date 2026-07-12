from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,                # means field is required
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Vineet Singh"]
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000
    )
    email: str = Field(..., pattern=r'^[a-z]+@[a-z]+\.com$')

emp1 = {
    "id": 123,
    "name": "Vineet Singh",
    "salary": 40_000,
    "email": "vineet@gmail.com"
}
try:
    cart_valid = Employee(**emp1)
    print("Valid data (no error raised)")
except Exception as e:
    print("Invalid data (error raised):", e)