from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr = Field(..., example ="nilsjohn6@gmail.com")
    first_name: str = Field(..., example="Nils")
    last_name: str = Field(..., example="Olsson")
    password: str = Field(..., example="bacon0101")

class UserOut(BaseModel):
    user_id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    created_at: datetime
    
    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(..., example = "nils.cool1@hotmail.com")
    first_name: Optional[str] = Field(..., example = "Emil")
    last_name: Optional[str] = Field(..., example = "Appelgren")
    password: Optional[str] = Field(..., example = "Bacon_0101")

    class Config:
        extra = "forbid"

class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="nilsjohn6@gmail.com")
    password: str = Field(..., example="bacon0101")
