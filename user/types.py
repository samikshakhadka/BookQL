# user/types.py
import strawberry
import strawberry_django
from strawberry import auto
from . import models
from typing import Optional
from django.db.models import Q

#filter

@strawberry_django.filters.filter(models.CustomUser, lookups=True)
class UserFilter:
    id: auto
    email: auto
    first_name: auto

    @strawberry_django.filter_field
    def special_filter(self, prefix: str, value: str):
        return Q(**{f"{prefix}name": value})

@strawberry_django.ordering.order(models.CustomUser)
class UserOrder:
    name: auto
    

@strawberry_django.type(models.CustomUser,
                        filters=UserFilter,
                        order=UserOrder,
                        pagination=True,)
class UserType:
    id: strawberry.ID
    email: auto 
    first_name: auto
    last_name: auto
    password: auto
    is_staff: auto
    date_joined: auto
    is_verified: auto
    verification_token: auto
    is_superuser: auto


@strawberry_django.type(models.CustomUser)
class meType:
    id: strawberry.ID
    
@strawberry_django.input(models.CustomUser)
class RegisterInput:
    
    email: auto
    first_name: auto
    last_name: auto
    password: auto
    is_staff: auto
    is_verified: auto
    verification_token: auto
    is_superuser: auto

@strawberry_django.input(models.CustomUser)
class UserInput:
    
    email: auto
    first_name: auto
    last_name: auto
    password: auto
    is_staff: auto
    is_verified: auto
    verification_token: auto
    is_superuser: auto

@strawberry_django.input(models.CustomUser)
class LoginInput:
    email : str
    password : str

@strawberry_django.input(models.CustomUser)
class UserUpdateInput:
    
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_verified: Optional[bool] = None
    
