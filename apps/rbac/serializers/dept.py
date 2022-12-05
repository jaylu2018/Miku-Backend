from rest_framework import serializers
from apps.rbac.models.dept import Dept


class DeptSerializer(serializers.ModelSerializer):
    """
    组织架构序列化
    """
    # type = serializers.ChoiceField(choices=Dept.organization_type_choices, default='department')

    class Meta:
        model = Dept
        fields = '__all__'
