# import strawberry_django
# from book.schema import BookQuery, BookMutation
# from user.schema import UserQuery, UserMutation

# @strawberry_django.type
# class Query(BookQuery, UserQuery):
#     pass

# @strawberry_django.type
# class Mutation(BookMutation, UserMutation):
#     pass

# schema = strawberry_django.Schema(query=Query, mutation=Mutation)

import strawberry
from book.schema import BookQuery, BookMutation
from user.schema import UserQuery, UserMutation

@strawberry.type
class Query(BookQuery, UserQuery):
    pass

@strawberry.type
class Mutation(BookMutation, UserMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation
)
