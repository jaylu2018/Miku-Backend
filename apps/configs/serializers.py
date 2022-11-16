from rest_framework import serializers
from .models import Envs
from utils.common import tools


class EnvsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
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
