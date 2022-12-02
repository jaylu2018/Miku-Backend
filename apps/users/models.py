from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from utils.validators import MobileValidator


class User(AbstractUser):
    """
    继承原有的用户模型，添加手机号字段
    """
    mobile_validator = MobileValidator()
    mobile = models.CharField(
        _("mobile"),
        max_length=11,
        unique=False,
        help_text='手机号',
        validators=[mobile_validator],
        error_messages={'unique': '手机号已存在'}
    )

    class Meta:
        db_table = 'tb_user'  # 指定模型对应的表名
        verbose_name = _('用户表')  # admin后台显示的表名
        verbose_name_plural = _('用户表')  # admin后台显示的表名的复数形式

    REQUIRED_FIELDS = ['mobile']  # 创建超级用户时需要输入的字段
