from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

try:
    product_1 = Product(id=1, name="Laptop", price=999.99, in_stock=True)
    product_2 = Product(id=2, name="Mouse", price=24.33)
    product_3 = Product(name="keyboard")    # will raise error
except Exception as e:      # way to get all errors
    print("Invalid data!")