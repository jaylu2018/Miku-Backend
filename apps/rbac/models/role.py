from django.db import models

from utils.models.base_models import BaseModel
from apps.rbac.models.permission import Permission
from apps.rbac.models.menu import Menu


class Role(BaseModel):
    """
    角色
    """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色名称")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="权限")
    menus = models.ManyToManyField("Menu", blank=True, verbose_name="菜单")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")
    status = models.BooleanField(default=True, verbose_name="角色状态", help_text="角色状态")
    is_admin = models.BooleanField(default=False, verbose_name="是否为admin", help_text="是否为admin")
