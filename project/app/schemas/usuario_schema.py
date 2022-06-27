from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class AuthUserSchema(BaseModel):
    id : Optional[int] = None
    username : str
    password : str
    first_name : str
    last_name : str
    email : str   
    is_active = str
    
    class Config:
        orm_mode = True
        