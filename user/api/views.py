from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from user.serializers import *
from user.models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]