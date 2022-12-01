import re

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_mobile(value):
    if not re.match(r'1[3-9]\d{9}', value):
        raise ValidationError('手机号码格式不正确')


class User(AbstractUser):
    """
    自定义用户模型
    添加mobile字段到用户模型中
    """
    mobile = models.CharField(
        '手机号码', max_length=11, unique=True, help_text='手机号码',
        error_messages={'unique': '手机号码已注册'},
        validators=[validate_mobile]
    )

    class Meta:
        db_table = 'tb_user'  # 表名
        verbose_name = '用户表'  # 站点显示名称
        verbose_name_plural = verbose_name  # 复数显示

    REQUIRED_FIELDS = ['mobile']  # 再通过createsuperuser 管理命令创建用户时，会提示输入mobile字段
