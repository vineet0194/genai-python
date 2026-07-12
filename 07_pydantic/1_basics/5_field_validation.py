from pydantic import BaseModel, field_validator, model_validator

# @field_validator - validates one field at a time.

class User(BaseModel):
    uid: int
    username: str

    # you need to specify what attributes the field validator can access
    @field_validator("username", mode="after")
    def username_length(cls, value):
        if (len(value) < 4):
            raise ValueError("Username must be at least 4 chars")
        return value



# ! what are modes?
    # mode="before" --> Runs before Pydantic validates the field(s).
    # mode="after" --> Runs after all field validation and type conversion.



# @model_validator - validates the entire object.

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    # model validator has access to all attributes at the same time
    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values
    

# ! why do i need these validators when i can simply define fields and do try-except?

# That's a very good question. The answer is: You can use try/except alone, but validators let you keep your validation rules inside the model instead of scattering them throughout your code.