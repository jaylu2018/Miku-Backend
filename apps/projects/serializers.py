from rest_framework import validators
from rest_framework import serializers
from .models import Projects
from utils.common import tools
from ..interfaces.models import Interfaces


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        # exclude = ('update_time',)

        extra_kwargs = {
            'create_time': {
                # 'read_only': True,
                'format': tools.datetime_fmt(),
            },
            'update_time': {
                # 'read_only': True,
                'format': tools.datetime_fmt(),
            },
        }


class ProjectsNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfacesNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class InterfacesByProjectsIdModelSerializer(serializers.ModelSerializer):
    interfaces = InterfacesNamesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = ('interfaces',)

