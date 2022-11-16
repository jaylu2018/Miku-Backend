from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.responses.base_response import APIResponse, NaiveResponse
from .serializers import RegisterSerializer, PersonSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        return APIResponse(data=serializer.data, msg='注册成功', code=200, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        datas = super().post(request, *args, **kwargs)
        data = {
            "nickName": "超级管理员",
            "userName": "admin",
            "userId": 1,
            "roleId": 1,
            "token": datas.data['access'],
            "roles": [
                {
                    "roleCode": "ROLE_admin",
                    "roleId": 1,
                    "roleName": "超级管理员"
                }
            ]
        }
        # return APIResponse(data=data, msg='登陆成功', code=200, status=status.HTTP_201_CREATED)
        return NaiveResponse(data=data, msg='登陆成功', code=200, status=status.HTTP_200_OK)


class UserView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = User.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        super().retrieve(request, *args, **kwargs)
        data = {
            "id": 1, "createTime": "2021-02-24 21:16:41", "updateTime": "2021-02-27 18:21:16",
            "departmentId": "1", "name": "超级管理员", "username": "admin", "passwordV": 3, "nickName": "管理员",
            "headImg": "https://ci.xiaohongshu.com/7db882e3-9cd1-3e0c-6129-977321bdfc4d?imageView2/2/w/1080/format/jpg",
            "phone": "18000000000", "email": "team@cool-js.com", "remark": "拥有最高权限的用户", "status": 1,
            "socketId": ''
        }
        return APIResponse(data=data, msg='success', code=200, status=status.HTTP_201_CREATED)

