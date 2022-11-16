from rest_framework import serializers
from .models import Menu


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('userId', 'roleId')
