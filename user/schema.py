from typing import List
from dataclasses import asdict
import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from .types import UserInput, UserUpdateInput , UserType
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist

# @strawberry.type
# class UserQuery:
#     user: UserType = strawberry_django.field()
#     users: list[UserType] = strawberry_django.field()

#     def resolve_user(self, info, email: str) -> UserType:
#         try:
#             return CustomUser.objects.get(email=email)
#         except ObjectDoesNotExist:
#             raise Exception("User not found")

#     def resolve_users(self, info) -> list[UserType]:
#         return CustomUser.objects.all()


@strawberry.type
class UserMutation:
    create_user: UserType = strawberry_django.mutations.create(UserInput)

    @strawberry.mutation
    def update_user(self, id: int, data: UserUpdateInput) -> UserType:
        try:
            user = CustomUser.objects.get(id=id)
            for key, value in asdict(data).items():
                if value is not None:
                    setattr(user, key, value)

            user.save()

            return user
        except CustomUser.DoesNotExist:
            raise Exception("Not Found")


    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        try:
            user = CustomUser.objects.get(pk=id)
            user.delete()

            return True
        except CustomUser.DoesNotExist:
            raise Exception("Not Found")



@strawberry.type
class UserQuery:
    books: List[UserType] = strawberry_django.field()


schema = strawberry.Schema(query=UserQuery, mutation=UserMutation)















# @strawberry.type
# class UserMutation:
#     @strawberry.mutation
#     def create_user(self, info, email: str, password: str, first_name: str = '', last_name: str = '') -> UserType:
#         try:
#             user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
#             return user
#         except Exception as e:
#             raise Exception(f"Error creating user: {str(e)}")

#     @strawberry.mutation
#     def update_user(self, info, email: str, first_name: str = None, last_name: str = None) -> UserType:
#         try:
#             user = CustomUser.objects.get(email=email)
#             if first_name is not None:
#                 user.first_name = first_name
#             if last_name is not None:
#                 user.last_name = last_name
#             user.save()
#             return user
#         except ObjectDoesNotExist:
#             raise Exception("User not found")
#         except Exception as e:
#             raise Exception(f"Error updating user: {str(e)}")

#     @strawberry.mutation
#     def delete_user(self, info, email: str) -> bool:
#         try:
#             user = CustomUser.objects.get(email=email)
#             user.delete()
#             return True
#         except ObjectDoesNotExist:
#             raise Exception("User not found")
#         except Exception as e:
#             raise Exception(f"Error deleting user: {str(e)}")

# schema = strawberry.Schema(
#     query=UserQuery,
#     mutation=UserMutation,
#     extensions=[
#         DjangoOptimizerExtension,  # Not required, but recommended
#     ],
# )