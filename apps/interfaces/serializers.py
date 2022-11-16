from rest_framework import serializers
from apps.interfaces.models import Interfaces
from apps.projects.models import Projects


class InterfacesModelSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField(label='所属项目名称', help_text='所属项目名称')
    # project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),
    #                                                 label='项目id', help_text='项目id', )

    class Meta:
        model = Interfaces
        # fields = ('id', 'name', 'tester', 'create_time', 'desc', 'project', 'project_id')
        fields = '__all__'

        # extra_kwargs = {
        #     'create_time': {
        #         'read_only': True,
        #         # 'format': common.datetime_fmt()
        #     }
        # }
