"""
This file contains entities for field validation for different actions. It does the same logic as serializers in DRF
"""
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
