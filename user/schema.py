from typing import List
from dataclasses import asdict
import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension
from .types import  UserUpdateInput , UserType, RegisterInput , LoginInput , UserInput
from .models import CustomUser
from strawberry_django.resolvers import django_resolver
from strawberry.types import Info
from strawberry_django.utils.requests import get_request



from strawberry_django import auth, mutations

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from strawberry.types import Info
import strawberry
from .models import CustomUser
from .types import UserType
from strawberry_django import mutations

import uuid
from asgiref.sync import sync_to_async

from django.contrib.auth import get_user_model



@strawberry.type
class CustomAuthPayload:
    user: UserType
    token: str

# def authenticate(email=None, password=None, **kwargs):
#             UserModel = CustomUser
#             try:
#                 user = UserModel.objects.get(email=email)
#                 if user.check_password(password):
#                     return user
#             except UserModel.DoesNotExist:
#                 return None

@strawberry.type
class UserMutation:
     
    
        
    @strawberry.mutation
    async def login(self, info: Info, input: LoginInput) -> CustomAuthPayload:
        request = info.context["request"]
        print(" 999999999999999", request)
        print("Input email:", input.email)

        user = await sync_to_async(authenticate)(request, email=input.email, password=input.password)
        print('000000000000', user)
        if not user:                                                                                                                                                                                                                                                                        
            raise ValidationError("Invalid email or password")

        if not user.verification_token:
            user.verification_token = uuid.uuid4()
            await sync_to_async(user.save)()

        token = user.verification_token
    
        await sync_to_async(update_last_login)(None, user)
        return CustomAuthPayload(user=user, token=token)


    # login: UserType = strawberry_django.auth.login()

    logout = strawberry_django.auth.logout()
    register: UserType = strawberry_django.auth.register(RegisterInput)
    
    create_user: UserType = mutations.create(UserInput)
    
    update_user : List[UserType] = mutations.update(UserUpdateInput)

    delete_user : List[UserType]= mutations.delete()

    #register: User = auth.register(RegisterInput)


    # @strawberry.mutation
    # def update_user(self, id: int, data: UserUpdateInput) -> UserType:
    #     try:
    #         user = CustomUser.objects.get(id=id)
    #         for key, value in asdict(data).items():
    #             if value is not None:
    #                 setattr(user, key, value)

    #         user.save()

    #         return user
    #     except CustomUser.DoesNotExist:
    #         raise Exception("Not Found")


    # @strawberry.mutation
    # def delete_user(self, id: int) -> bool:
    #     try:
    #         user = CustomUser.objects.get(pk=id)
    #         user.delete()

    #         return True
    #     except CustomUser.DoesNotExist:
    #         raise Exception("Not Found")



@strawberry.type
class UserQuery:
    me: UserType = strawberry_django.auth.current_user()

    user: UserType = strawberry_django.field()

    user: List[UserType] = strawberry_django.field()


schema = strawberry.Schema(query=UserQuery, mutation=UserMutation)















