from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]            # list of strings
    quantities: Dict[str, int]    # dict with k-v pair as string-int

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None     # optional, if present => it will be a string, by default = None

cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {
        "laptop": 1,
        "mouse": 2,
        "keyboard": 3
    }
}

try:
    cart_valid = Cart(**cart_data)
    print("Valid data (no error raised)")
except Exception as e:
    print("Invalid data (error raised):", e)