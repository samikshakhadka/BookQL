# context.py
from strawberry.types import Info

class CustomContext:
    def __init__(self, request):
        self.request = request
        self.user = request.user

# context getter function
def get_context(request):
    return CustomContext(request=request)
