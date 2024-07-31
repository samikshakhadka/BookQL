# project/urls.py

from django.contrib import admin
from django.urls import path, include
from config.schema import schema


from strawberry.django.views import AsyncGraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', AsyncGraphQLView.as_view(schema=schema)),
]
