from rest_framework import serializers
from apps.rbac.models.dept import Dept


class DeptSerializer(serializers.ModelSerializer):
    """
    组织架构序列化
    """
    children = serializers.SerializerMethodField()

    def get_children(self, obj: Dept):
        departments = Dept.objects.filter(parent_id=obj.id)
        tree = []
        for department in departments:
            tree.append(Dept.objects.filter(id=department.id).values()[0])
        return tree

    class Meta:
        model = Dept
        fields = '__all__'
