from pydantic import BaseModel, EmailStr
from typing import Literal

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Literal["admin", "staff"]

class UserRead(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True
