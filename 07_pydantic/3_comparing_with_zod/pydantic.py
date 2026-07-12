from pydantic import BaseModel, Field, field_validator
import re

class User(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=10
    )

    first_name: str = Field(
        ...,
        max_length=15
    )

    last_name: str = Field(
        ...,
        max_length=15
    )

    password: str = Field(
        ...,
        min_length=6
    )

    @field_validator("username", mode="before")
    def normalize_username(cls, value):
        return value.strip().lower()

    @field_validator("username")
    def validate_username(cls, value):
        if not re.fullmatch(r"[a-z0-9]+", value):
            raise ValueError(
                "Username can only contain lowercase letters (a-z) and numbers (0-9)"
            )
        return value

    @field_validator("first_name", "last_name", mode="before")
    def trim_names(cls, value):
        return value.strip()

    @field_validator("first_name", "last_name")
    def validate_names(cls, value):
        if not re.fullmatch(r"[a-zA-Z]+", value):
            raise ValueError("Name can only contain letters")
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one number")

        if not re.search(r"[^\w\s]", value):
            raise ValueError("Password must contain at least one special character")

        return value