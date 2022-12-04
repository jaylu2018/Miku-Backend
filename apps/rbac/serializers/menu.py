from rest_framework import serializers
from apps.rbac.models.menu import Menu


class MenuSerializer(serializers.ModelSerializer):
    """
    菜单
    """

    class Meta:
        model = Menu
        fields = ('id', 'name', 'icon', 'path', 'is_show', 'is_frame', 'sort', 'component', 'pid')
        extra_kwargs = {
            'name': {
                'required': True,
                'error_messages': {'required': '必须填写菜单名'}
            }
        }
