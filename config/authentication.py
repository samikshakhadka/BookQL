# user/authentication.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from user.models import CustomUser

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = CustomUser
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
