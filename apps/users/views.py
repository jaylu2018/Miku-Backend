from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.models import User
from apps.users.serializers import MyTokenSerializer, MyTokenRefreshSerializer, RegisterSerializer, UserSerializer
from utils.permissions import SuperUserPermission


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')  # 按时间倒序
    # permission_classes = [SuperUserPermission]
