from rest_framework import serializers
from apps.rbac.models.dept import Dept


class SubDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = '__all__'


class DeptSerializer(serializers.ModelSerializer):
    """
    组织架构序列化
    """
    children = SubDeptSerializer(many=True, read_only=True)

    class Meta:
        model = Dept
        fields = '__all__'
