import re

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_mobile(value):
    if not re.match(r'1[3-9]\d{9}', value):
        raise ValidationError('手机号码格式不正确')


class User(AbstractUser):
    """
    继承原有的用户模型，添加手机号字段
    """
    mobile = models.CharField(
        max_length=11,
        unique=True,
        help_text='手机号',
        verbose_name='手机号',
        validators=[validate_mobile],
        error_messages={'unique': '手机号已存在'}
    )

    class Meta:
        db_table = 'tb_user'  # 指定模型对应的表名
        verbose_name = '用户表'  # admin后台显示的表名
        verbose_name_plural = verbose_name  # admin后台显示的表名的复数形式

    REQUIRED_FIELDS = ['mobile']  # 创建超级用户时需要输入的字段
