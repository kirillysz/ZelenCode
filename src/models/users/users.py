from src.models.users.users_role import UserRole

from pydantic import BaseModel, EmailStr, UUID4
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: UUID4
    email: EmailStr
    password_hash: Optional[str] = None
    oauth_provier: Optional[str] = None
    oauith_id: Optional[str] = None
    role: UserRole
    name: Optional[str] = None
    nickname: Optional[str] = None
    rating: int = 0
    created_at: datetime
    updated_at: datetime
    solved_tasks: Optional[List[UUID4]] = []
    stats: Optional[List[int, int]] = []