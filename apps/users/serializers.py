from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    error_messages_password_confirm = '仅允许6~20个字符的确认密码'
    password_confirm = serializers.CharField(
        label='确认密码', help_text='确认密码', min_length=6, max_length=20,
        write_only=True, error_messages={
            'min_length': error_messages_password_confirm,
            'max_length': error_messages_password_confirm,
        })
    token = serializers.CharField(label='生成token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 4,
                'max_length': 20,
                'error_messages': {
                    'min_length': '用户名长度不能小于6',
                    'max_length': '用户名长度不能大于20',
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 添加邮箱重复校验
                # 'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')],
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '密码长度不能小于6',
                    'max_length': '密码长度不能大于20',
                }
            }
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('密码与确认密码不一致')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        # 创建user模型对象
        user = User.objects.create_user(**validated_data)
        return user


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
