from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class Exercise(BaseModel):
    id: str
    exercise_name: str
    used_equipment: str
    prim_muscle: str
    sec_muscles: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLoign(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    id: Optional[str] = None