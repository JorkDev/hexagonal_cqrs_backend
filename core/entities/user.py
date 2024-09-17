from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class User(BaseModel):
    id: Optional[UUID]
    username: str
    email: str
