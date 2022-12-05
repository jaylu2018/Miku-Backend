from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from apps.rbac.models.dept import Dept
from apps.rbac.serializers.dept import DeptSerializer
from utils.responses.base_response import VbenResponse


class DeptViewSet(ModelViewSet):
    """
    部门管理：增删改查
    """
    serializer_class = DeptSerializer
    queryset = Dept.objects.all().order_by('-update_time')  # 按时间倒序

    def list(self, request, *args, **kwargs):
        data = super().list(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_201_CREATED, type_res='success')

    def update(self, request, *args, **kwargs):
        data = super().update(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')

    def destroy(self, request, *args, **kwargs):
        data = super().destroy(request, *args, **kwargs)
        return VbenResponse(data=data.data, msg='ok', code=0, status=status.HTTP_200_OK, type_res='success')
