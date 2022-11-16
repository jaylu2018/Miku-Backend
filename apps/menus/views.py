import json

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from utils.responses.base_response import APIResponse
from .models import Menu
from .serializers import MenusSerializer


class MenusView(ModelViewSet):
    serializer_class = MenusSerializer
    queryset = Menu.objects.all().order_by('-userId')

    def retrieve(self, request, *args, **kwargs):
        super().retrieve(request, *args, **kwargs)
        data = []
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        data = [
            {
                "menuUrl": "/projects",
                "menuName": "接口测试",
                "iconPrefix": "iconfont",
                "icon": "detail",
                "parentPath": "",
                "children": [
                    {
                        "parentPath": "/projects",
                        "menuUrl": "/projects/list",
                        "menuName": "项目列表",
                    },
                ]
            },
            {
                "menuUrl": "/system",
                "menuName": "系统管理",
                "iconPrefix": "iconfont",
                "icon": "setting",
                "parentPath": "",
                "children": [
                    {
                        "parentPath": "/system",
                        "menuUrl": "/system/role",
                        "menuName": "接口管理",
                        "buttonList": [
                            {
                                "name": "添加",
                                "code": "add",
                                "roleCode": "ROLE_admin",
                                "placement": "top",
                                "type": "primary"
                            },
                            {
                                "name": "编辑",
                                "code": "update",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "warning"
                            },
                            {
                                "name": "删除",
                                "code": "delete",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "error"
                            },
                            {
                                "name": "菜单管理",
                                "code": "menu",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "success"
                            }
                        ]
                    },
                    {
                        "parentPath": "/system",
                        "menuUrl": "/system/user",
                        "menuName": "案例管理",
                        "buttonList": [
                            {
                                "name": "添加",
                                "code": "add",
                                "roleCode": "ROLE_admin",
                                "placement": "top",
                                "type": "primary"
                            },
                            {
                                "name": "编辑",
                                "code": "update",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "warning"
                            },
                            {
                                "name": "删除",
                                "code": "delete",
                                "roleCode": "ROLE_admin",
                                "placement": "default",
                                "type": "error"
                            }
                        ]
                    },
                ]
            },
            {
                "menuUrl": "/tool",
                "menuName": "工具",
                "iconPrefix": "iconfont",
                "icon": "file-unknown",
                "parentPath": "",
                "children": [
                    {
                        "parentPath": "/tool",
                        "menuUrl": "/tool/success",
                        "menuName": "成功页面"
                    },
                ]
            }
        ]
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)


class MenusView2(ModelViewSet):
    serializer_class = MenusSerializer
    queryset = Menu.objects.all().order_by('-userId')

    def retrieve(self, request, *args, **kwargs):
        super().retrieve(request, *args, **kwargs)
        data = []
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        data = [
            {
                "menuUrl": "/projects",
                "menuName": "接口测试",
                "iconPrefix": "iconfont",
                "icon": "detail",
                "parentPath": "",
                "children": [
                    {
                        "parentPath": "/projects",
                        "menuUrl": "/projects/list",
                        "menuName": "项目列表",
                    },
                ]
            },
            {
                "menuUrl": "/system",
                "menuName": "系统管理",
                "iconPrefix": "iconfont",
                "icon": "setting",
                "parentPath": "",
                "children": [
                    {
                        "parentPath": "/system",
                        "menuUrl": "/system/role",
                        "menuName": "接口管理",
                        "buttonList": [
                            {
                                "name": "添加",
                                "code": "add",
                                "roleCode": "ROLE_admin",
                                "placement": "top",
                                "type": "primary"
                            },
                            {
                                "name": "编辑",
                                "code": "update",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "warning",
                            },
                            {
                                "name": "删除",
                                "code": "delete",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "error"
                            },
                            {
                                "name": "菜单管理",
                                "code": "menu",
                                "roleCode": "ROLE_admin",
                                "placement": "tableLine",
                                "type": "success"
                            }
                        ]
                    },
                ]
            },
        ]
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)


class Department(ModelViewSet):
    serializer_class = MenusSerializer
    queryset = Menu.objects.all().order_by('-userId')

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        data = [
            {
                "id": 1,
                "name": "总裁办",
                "depCode": "dp_code_manager",
                "order": 1,
                "createTime": "2022-02-20 19:41:15",
                "status": 0
            },
            {
                "id": 2,
                "name": "市场部",
                "depCode": "dp_code_marketing",
                "order": 1,
                "createTime": "2022-02-20 19:41:15",
                "status": 1,
                "children": [
                    {
                        "id": 3,
                        "parentId": 2,
                        "name": "市场一部",
                        "depCode": "dp_code_marketing_1",
                        "order": 1,
                        "createTime": "2022-02-20 19:41:15",
                        "status": 1
                    },
                    {
                        "id": 4,
                        "parentId": 2,
                        "name": "市场二部",
                        "depCode": "dp_code_marketing_2",
                        "order": 1,
                        "createTime": "2022-02-20 19:41:15",
                        "status": 1
                    }
                ]
            },
            {
                "id": 5,
                "name": "技术部",
                "depCode": "dp_code_technology",
                "order": 1,
                "createTime": "2022-02-20 19:41:15",
                "status": 1
            }
        ]
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)


class Role(ModelViewSet):
    serializer_class = MenusSerializer
    queryset = Menu.objects.all().order_by('-userId')

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        data = [
            {
                "id": 1,
                "name": "商户进件结果查询接口",
                "protocol": "HTTP",
                "description": "这是一个接口描述",
                "path": "/v1/customer/access/query",
                "createTime": "2022-02-20 19:41:15"
            },
        ]
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)


class User(ModelViewSet):
    serializer_class = MenusSerializer
    queryset = Menu.objects.all().order_by('-userId')

    def list(self, request, *args, **kwargs):
        super().list(request, *args, **kwargs)
        data = [
            {
                "id": 1,
                "nickName": "商户进件查询正向案例",
                "priority": "P0",
                "status": "调试中",
                "creater": "admin",
                "updateTime": "2022-02-20 19:41:15",
            }
        ]
        return APIResponse(data=data, msg='获取菜单列表成功', code=200, status=status.HTTP_200_OK)
