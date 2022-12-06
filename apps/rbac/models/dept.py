from django.db import models

from utils.models.base_models import BaseModel
from django.utils.translation import gettext_lazy as _


class Dept(BaseModel):
    """
    部门表
    """
    name = models.CharField(max_length=60, verbose_name="部门名称")
    owner = models.CharField(max_length=32, verbose_name="负责人", null=True, blank=True, help_text="负责人")
    phone = models.CharField(max_length=32, verbose_name="联系电话", null=True, blank=True, help_text="联系电话")
    email = models.EmailField(max_length=32, verbose_name="邮箱", null=True, blank=True, help_text="邮箱")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")
    status = models.BooleanField(default=True, verbose_name="部门状态", null=True, blank=True, help_text="部门状态")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, verbose_name="上级部门")

    class Meta:
        db_table = 'tb_dept'  # 指定模型对应的表名
        verbose_name = _('部门表')  # admin后台显示的表名
        verbose_name_plural = _('部门表')  # admin后台显示的表名的复数形式

    def __str__(self):
        return self.name
