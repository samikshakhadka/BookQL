from typing import List
from dataclasses import asdict
import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from book.types import BookInput, Book, BookUpdateInput , FavoriteInput, FavoriteType, FavoriteUPdateInput

from strawberry.permission import BasePermission
from strawberry_django import mutations
from strawberry_django.permissions import (
    IsAuthenticated,
   
)

@strawberry.type
class BookMutation:

    
    create_book: Book = mutations.create(BookInput)

    update_book : List[Book] = mutations.update(BookUpdateInput)

    delete_book : List[Book] = mutations.delete()

    # @strawberry.mutation

    # def update_book(self, id: int, data: BookUpdateInput) -> BookType:
    #     try:
    #         book = Book.objects.get(id=id)
    #         for key, value in asdict(data).items():
    #             if value is not None:
    #                 setattr(book, key, value)

    #         book.save()

    #         return book
    #     except Book.DoesNotExist:
    #         raise Exception("Not Found")    

    # @strawberry.mutation
    # def delete_book(self, id: int) -> bool:
    #     try:
    #         user = Book.objects.get(pk=id)
    #         user.delete()

    #         return True
    #     except Book.DoesNotExist:
    #         raise Exception("Not Found")

@strawberry.type
class BookQuery:
    books: List[Book] = strawberry_django.field()


schema = strawberry.Schema(query=BookQuery, mutation=BookMutation)


















