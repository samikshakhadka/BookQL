import strawberry_django
from strawberry import auto

from user.types import UserType
from typing import Optional
from . import models

@strawberry_django.type(models.Book)
class Book:
    id: auto
    title: auto
    author: auto
    description: auto
    created_by: UserType
    created_at: auto
    updated_at: auto
    is_deleted: auto

@strawberry_django.type(models.Favorite)
class FavoriteType:
    id: auto
    user: UserType
    book: Book

@strawberry_django.input(models.Book)
class BookInput:
    
    title: auto
    author: auto
    description: auto
    created_by: UserType
    created_at: auto
    updated_at: auto
    is_deleted: auto

@strawberry_django.input(models.Book)
class BookUpdateInput:
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None

@strawberry_django.input(models.Favorite)
class FavoriteInput:
    user: UserType
    book: Book

@strawberry_django.input(models.Favorite)
class FavoriteUPdateInput:
    user: UserType | None = None
    book: Book| None = None



