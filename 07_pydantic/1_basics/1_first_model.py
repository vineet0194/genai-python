# Pydantic (similar to Zod in TS) - type hints providing Schema validation
# zod and pydantic both define a schema, validate input, and give you typed data back.
# provides Data Validation and Setting Management

# Pydantic performs type coercion by default, whereas Zod is strict unless you opt into coercion.
# !Type coercion means automatically converting input values to the expected type when the conversion is
# valid (e.g., string → integer, string → boolean). Pydantic performs this by default to make working with
# external data easier, whereas Zod is strict by default and requires the input type to already match
# unless you explicitly enable coercion.

# Zod returns an object like { success: true/false, data, error }, whereas Pydantic raises an exception
# if validation fails. You handle that exception to achieve similar behavior, using try-except

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    "id": "101",
    "name": "ChaiCode",
    "is_active": True
}

user = User(**input_data)   # passed unpacked data
print(user)