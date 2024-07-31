# user/types.py

import strawberry_django
from strawberry import auto
from . import models
from typing import Optional

@strawberry_django.type(models.CustomUser)
class UserType:
    id: auto
    email: auto
    first_name: auto
    last_name: auto
    is_staff: auto
    date_joined: auto
    is_verified: auto
    verification_token: auto
    is_superuser: auto

@strawberry_django.input(models.CustomUser)
class UserInput:
    
    email: auto
    first_name: auto
    last_name: auto
    is_staff: auto
    is_verified: auto
    verification_token: auto
    is_superuser: auto

@strawberry_django.input(models.CustomUser)
class UserUpdateInput:
    
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_verified: Optional[bool] = None
    
