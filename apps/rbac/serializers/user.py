from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(
        min_length=4,
        max_length=16,
        write_only=True,
        label='确认密码',
        help_text='确认密码',
        error_messages={
            'min_length': '密码长度小于6位',
            'max_length': '密码长度大于20位'
        }
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirm', 'email', 'mobile')
        # 对于模型中已经存在的字段，可以通过extra_kwargs扩展一下额外的限制
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 4,
                'max_length': 16,
                'error_messages': {
                    'min_length': '用户名长度小于4位',
                    'max_length': '用户名长度大于16位'
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 添加邮箱重复校验
                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')],
            },
            'mobile': {
                'label': '手机号',
                'help_text': '手机号',
                'write_only': True,
                'required': False
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'min_length': 4,
                'max_length': 16,
                'write_only': True,
                'error_messages': {
                    'min_length': '密码长度小于4位',
                    'max_length': '密码长度大于16位'
                }
            },
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('两次密码不一致')
        attrs.pop('password_confirm')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'mobile', 'email', 'is_active', 'is_superuser')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        # 手动的处理密码
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        obj = super().update(instance, validated_data)
        # 手动的处理密码
        if validated_data.get('password'):
            obj.set_password(validated_data['password'])
            obj.save()
        return obj
