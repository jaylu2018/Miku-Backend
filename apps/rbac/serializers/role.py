from rest_framework import serializers
from apps.rbac.models.role import Role


class RoleSerializer(serializers.ModelSerializer):
    """
    角色
    """

    class Meta:
        model = Role
        fields = '__all__'
