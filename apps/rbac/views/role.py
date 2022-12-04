from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from apps.rbac.models.role import Role
from apps.rbac.serializers.role import RoleSerializer, RoleModifySerializer

from utils.permissions import SuperUserPermission
from utils.responses.base_response import VbenResponse


class RoleViewSet(ModelViewSet):
    """
    角色管理：增删改查
    """
    serializer_class = RoleSerializer
    queryset = Role.objects.all().order_by('-update_time')  # 按时间倒序

    # permission_classes = [SuperUserPermission]
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
