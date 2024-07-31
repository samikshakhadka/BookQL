import strawberry_django
from strawberry import auto
from .models import Book, Favorite
from user.types import UserType
from typing import Optional

@strawberry_django.type(Book)
class BookType:
    id: auto
    title: auto
    author: auto
    description: auto
    created_by: UserType
    created_at: auto
    updated_at: auto
    is_deleted: auto

@strawberry_django.type(Favorite)
class FavoriteType:
    id: auto
    user: UserType
    book: BookType

@strawberry_django.input(Book)
class BookInput:
    
    title: auto
    author: auto
    description: auto
    created_by: UserType
    created_at: auto
    updated_at: auto
    is_deleted: auto

@strawberry_django.input(Book)
class BookUpdateInput:
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None

@strawberry_django.input(Favorite)
class FavoriteInput:
    user: UserType
    book: BookType

@strawberry_django.input(Favorite)
class FavoriteUPdateInput:
    user: UserType | None = None
    book: BookType | None = None



