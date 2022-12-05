from django.db import models

from utils.models.base_models import BaseModel
from django.utils.translation import gettext_lazy as _


class Role(BaseModel):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色名称")
    # permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限")
    # menus = models.ManyToManyField("Menu", blank=True, verbose_name="菜单")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")
    status = models.BooleanField(default=True, verbose_name="角色状态", help_text="角色状态")
    is_admin = models.BooleanField(default=False, verbose_name="是否为admin", help_text="是否为admin")

    class Meta:
        db_table = 'tb_role'  # 指定模型对应的表名
        verbose_name = _('角色表')  # admin后台显示的表名
        verbose_name_plural = _('角色表')  # admin后台显示的表名的复数形式

    def __str__(self):
        return self.name
