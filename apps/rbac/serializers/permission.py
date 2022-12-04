from rest_framework import serializers
from apps.rbac.models.permission import Permission


class PermissionListSerializer(serializers.ModelSerializer):
    """
    权限列表序列化
    """
    menuname = serializers.ReadOnlyField(source='menus.name')

    class Meta:
        model = Permission
        fields = ('id', 'name', 'method', 'menuname', 'pid')
