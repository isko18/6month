from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import CustomUser
from apps.users.serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]