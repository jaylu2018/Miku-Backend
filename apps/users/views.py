from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from apps.users.models import User
from apps.users.serializers import RegisterSerializer, UserSerializer
from utils.permissions import SuperUserPermission
from utils.responses.base_response import VbenResponse


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        datas = super().post(request, *args, **kwargs)
        data = {
            "userId": '1',
            "username": 'miku',
            "realName": 'Miku',
            "avatar": 'https: //q1.qlogo.cn/g?b=qq&nk=190848757&s=640',
            "desc": 'manager',
            "password": '123456',
            "token": 'fakeToken1',
            "homePath": '/dashboard/analysis',
            "roles": [
                {
                    "roleName": 'Super Admin',
                    "value": 'super'
                }
            ]
        }
        return VbenResponse(data=data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-date_joined')  # 按时间倒序
    # permission_classes = [SuperUserPermission]

    def retrieve(self, request, *args, **kwargs):
        super().retrieve(request, *args, **kwargs)
        data = {
            "userId": "1",
            "username": "miku",
            "realName": "Miku",
            "avatar": "https://q1.qlogo.cn/g?b=qq&nk=190848757&s=640",
            "desc": "manager",
            "password": "123456",
            "token": "fakeToken1",
            "homePath": "/dashboard/analysis",
            "roles": [
                {
                    "roleName": "Super Admin",
                    "value": "super"
                }
            ]
        }
        return VbenResponse(data=data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')
