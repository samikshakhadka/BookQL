from typing import List

import strawberry
import strawberry_django
from .types import  UserUpdateInput , UserType, RegisterInput , LoginInput , UserInput
from . import models

from strawberry.types import Info
from .context import get_context

from .models import CustomUser

from strawberry_django import auth, mutations

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import update_last_login
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from strawberry.types import Info
import strawberry
from .types import UserType
from strawberry_django import mutations

import uuid

from asgiref.sync import sync_to_async
from django.contrib.sessions.models import Session

from django.http import HttpRequest
from typing import Annotated, Union

@strawberry.type
class CustomAuthPayload:
    user: UserType
    



# @strawberry.type
# class LoginSuccess:
#     user: models.CustomUser
# @strawberry.type
# class LoginError:
#     message: str
# LoginResult = Annotated[Union[LoginSuccess, LoginError], strawberry.union("LoginResult")]
 

@strawberry.type
class UserMutation:
    # @strawberry.mutation
    # @sync_to_async
    # def login(self, info, email: str, password: str) -> CustomAuthPayload:
    #     user = authenticate(email=email, password=password)
    #     if user is None:
    #         raise ValidationError("Invalid email or password")
    #     # info.context.request.session['email'] = user.email
    #     info.context.request.session['email'] = user.email
    #     info.context.request.session.save()
    #     return CustomAuthPayload(user=user)
    

    # def login(self, request,email: str, password: str) -> LoginResult:
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return LoginSuccess(user=models.CustomUser(email=email))
    #     return LoginError(message="Invalid credentials")
        
    @strawberry.mutation
    async def login(self, info: Info, input: LoginInput) -> CustomAuthPayload:
        request = info.context["request"]
        print(" 999999999999999", request)
        print("Input email:", input.email)

        user = await sync_to_async(authenticate)(request, email=input.email, password=input.password)
        print('000000000000', user)
        if not user:
            raise ValidationError("Invalid email or password")

        await sync_to_async(login)(request, user)
        #request.session.save()

        print('Authenticated user:', user)
        print('Session data:', request.session.items())


        return CustomAuthPayload(user=user)


    @strawberry.mutation
    async def logout(self, info: Info) -> str:
        request = info.context["request"]


        # Logout the user
        await sync_to_async(logout)(request)

        # Clear the session data
        session_key = request.session.session_key
        if session_key:
            await sync_to_async(Session.objects.filter(session_key=session_key).delete)()

        # Redirect to home or return a success message
        return "User successfully logged out"


    # login: UserType = strawberry_django.auth.login()

    #logout = strawberry_django.auth.logout()
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




from typing import Optional
@strawberry.type
class UserQuery:

    

    # me: UserType = strawberry_django.auth.current_user()
    @strawberry.field
    @sync_to_async
    def me(self, info:Info) -> int:
        print("oooooooooooooooooooooo",info.context.request.user.id)
        return str(info.context.request.user.id)
    

    # @strawberry.field
    # @sync_to_async

    # def me(self,info: Info) -> Optional[UserType]:
    #     user = info.context.request.user
    #     # user_id = request.session.get('user_id')

    #     #print("rrrrrrrrrr8888888888888888888888888", request)
    #     # print("0000000000000000",self)

    #     # user = request.user
    #     print("9999999999999", user)
    #     # user = request.user
        
    #     # if user.is_authenticated:
    #     user_data = CustomUser.objects.get(id=user.id)
    #     return UserType(id=user_data.id, email=user_data.email, first_name=user_data.first_name)# Populate with additional user fields as needed
    #     return None


    # @strawberry.field
    # async def me(self, info: Info) -> Optional[UserType]:
    #     request = info.context.request
    #     user = request.user

    #     if user.is_authenticated:
    #         try:
    #             # Fetch user data using sync_to_async to avoid SynchronousOnlyOperation error
    #             user_data = await sync_to_async(lambda: models.CustomUser.objects.get(id=user.id))()
    #             return UserType(id=user_data.id, email=user_data.email, first_name=user_data.first_name)
    #         except models.CustomUser.DoesNotExist:
    #             # Log or handle the case where the user does not exist
    #             print("User does not exist.")
    #             return None

    #     # User is not authenticated or does not exist
    #     return None




    # @strawberry.field
    # @sync_to_async
    # def me(self, info: Info) -> Optional[UserType]:
    #     request = info.context["request"]
    #     print('rrrrrrrrrrrrrrrrrrrrrrrrrr', request)
    #     user = request.user
    #     print('ppppppppppppppppppppppppppppp', user)

    #     if user.is_authenticated:
    #         user_data = CustomUser.objects.get(id=user.id)()
    #         return UserType(id=user_data.id, email=user_data.email, first_name=user_data.first_name)

    #     return None


    # @strawberry.field
    # @sync_to_async
    # def current_user(self, info: Info) -> UserType:
    #     request = info.context["request"]
    #     user = request.user

    #     if not user.is_authenticated:
    #         raise Exception("User is not authenticated")

    #     return UserType(
    #         id=str(user.id),
    #         email=user.email,
    #         first_name=user.first_name,
    #         last_name=user.last_name
    #     )




    user: UserType = strawberry_django.field()

    user: List[UserType] = strawberry_django.field()


schema = strawberry.Schema(query=UserQuery, mutation=UserMutation)










