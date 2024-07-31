from typing import List
from dataclasses import asdict
import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from book.types import BookInput, BookType, BookUpdateInput , FavoriteInput, FavoriteType, FavoriteUPdateInput
from .models import Book, Favorite
#from user.models import CustomUser
from user.types import UserType  # Import the already defined UserType
from asgiref.sync import sync_to_async


@strawberry.type
class BookMutation:
    create_book: BookType = strawberry_django.mutations.create(BookInput)

    @strawberry.mutation

    def update_book(self, id: int, data: BookUpdateInput) -> BookType:
        try:
            book = Book.objects.get(id=id)
            for key, value in asdict(data).items():
                if value is not None:
                    setattr(book, key, value)

            book.save()

            return book
        except Book.DoesNotExist:
            raise Exception("Not Found")    

    @strawberry.mutation
    def delete_book(self, id: int) -> bool:
        try:
            user = Book.objects.get(pk=id)
            user.delete()

            return True
        except Book.DoesNotExist:
            raise Exception("Not Found")

@strawberry.type
class BookQuery:
    books: List[BookType] = strawberry_django.field()


schema = strawberry.Schema(query=BookQuery, mutation=BookMutation)


















# @strawberry.type
# class BookQuery:
#     books: list[BookType] = strawberry_django.field()
#     favorites: list[BookType] = strawberry_django.field()

#     def resolve_books(self, info) -> list[BookType]:
#         return Book.objects.filter(is_deleted=False)

#     def resolve_favorites(self, info, user_email: str) -> list[BookType]:
#         try:
#             user = CustomUser.objects.get(email=user_email)
#             return [favorite.book for favorite in Favorite.objects.filter(user=user)]
#         except CustomUser.DoesNotExist:
#             raise Exception("User not found")

# @strawberry.type
# class BookMutation:
#     # @strawberry.mutation
#     # def create_book(self, info, title: str, author: str, description: str, created_by_email: str) -> BookType:
#     #     try:
#     #         created_by = CustomUser.objects.get(email=created_by_email)
#     #         book = Book.objects.create(
#     #             title=title,
#     #             author=author,
#     #             description=description,
#     #             created_by=created_by
#     #         )
#     #         return book
#     #     except CustomUser.DoesNotExist:
#     #         raise Exception("User not found")
#     #     except Exception as e:
#     #         raise Exception(f"Error creating book: {str(e)}")
#     async def create_book(self, info, title: str, author: str, description: str, created_by_email: str) -> BookType:
#         try:
#             created_by = await sync_to_async(CustomUser.objects.get)(email=created_by_email)
#             book = await sync_to_async(Book.objects.create)(
#                 title=title,
#                 author=author,
#                 description=description,
#                 created_by=created_by
#             )
#             return book
#         except Exception as e:
#             raise Exception(f"Error creating book: {str(e)}")
        
#     @strawberry.mutation
#     async def update_book(self, info,id:int, title: str, new_title: str = None, new_author: str = None, new_description: str = None) -> BookType:
#         try:
#             book = await sync_to_async(Book.objects.get)(id=id)
#             if new_title is not None:
#                 book.title = new_title
#             if new_author is not None:
#                 book.author = new_author
#             if new_description is not None:
#                 book.description = new_description
#             await sync_to_async(book.save)()
#             return book
#         except Exception as e:
#             raise Exception(f"Error updating book: {str(e)}")

#     # @strawberry.mutation
#     # def delete_book(self, info, title: str) -> BookType:
#     #     try:
#     #         book = Book.objects.get(title=title)
#     #         book.is_deleted = True
#     #         book.save()
#     #         return book
#     #     except Book.DoesNotExist:
#     #         raise Exception("Book not found")
#     #     except Exception as e:
#     #         raise Exception(f"Error deleting book: {str(e)}")
#     @strawberry.mutation
#     async def delete_book(self, info, title: str) -> BookType:
#         try:
#             book = await sync_to_async(Book.objects.get)(title=title)
#             book.is_deleted = True
#             await sync_to_async(book.save)()
#             return book
#         except Exception as e:
#             raise Exception(f"Error deleting book: {str(e)}")

#     # @strawberry.mutation
#     # def favorite_book(self, info, user_email: str, book_title: str) -> FavoriteType:
#     #     try:
#     #         user = CustomUser.objects.get(email=user_email)
#     #         book = Book.objects.get(title=book_title)
#     #         favorite, created = Favorite.objects.get_or_create(user=user, book=book)
#     #         return favorite
#     #     except CustomUser.DoesNotExist:
#     #         raise Exception("User not found")
#     #     except Book.DoesNotExist:
#     #         raise Exception("Book not found")
#     #     except Exception as e:
#     #         raise Exception(f"Error favoriting book: {str(e)}")

#     # @strawberry.mutation
#     # def unfavorite_book(self, info, user_email: str, book_title: str) -> bool:
#     #     try:
#     #         user = CustomUser.objects.get(email=user_email)
#     #         book = Book.objects.get(title=book_title)
#     #         Favorite.objects.filter(user=user, book=book).delete()
#     #         return True
#     #     except CustomUser.DoesNotExist:
#     #         raise Exception("User not found")
#     #     except Book.DoesNotExist:
#     #         raise Exception("Book not found")
#     #     except Exception as e:
#     #         raise Exception(f"Error unfavoriting book: {str(e)}")

#     @strawberry.mutation
#     async def favorite_book(self, info, user_email: str, book_title: str) -> FavoriteType:
#         try:
#             user = await sync_to_async(CustomUser.objects.get)(email=user_email)
#             book = await sync_to_async(Book.objects.get)(title=book_title)
#             favorite, created = await sync_to_async(Favorite.objects.get_or_create)(user=user, book=book)
#             return favorite
#         except Exception as e:
#             raise Exception(f"Error favoriting book: {str(e)}")

#     @strawberry.mutation
#     async def unfavorite_book(self, info, user_email: str, book_title: str) -> bool:
#         try:
#             user = await sync_to_async(CustomUser.objects.get)(email=user_email)
#             book = await sync_to_async(Book.objects.get)(title=book_title)
#             await sync_to_async(Favorite.objects.filter(user=user, book=book).delete)()
#             return True
#         except Exception as e:
#             raise Exception(f"Error unfavoriting book: {str(e)}")
