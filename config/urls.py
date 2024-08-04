# project/urls.py

from django.contrib import admin
from django.urls import path, include
from config.schema import schema
from user.context import get_context


from strawberry.django.views import AsyncGraphQLView
from strawberry.django.views import GraphQLView as BaseGraphQLView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', AsyncGraphQLView.as_view(schema=schema)),
]

# class CustomGraphQLView(BaseGraphQLView):
#     def get_context(self, request, response):
#         return {"request": request, "response": response}

# urlpatterns = [
#     path('graphql/', CustomGraphQLView.as_view(schema=schema)),
# ]