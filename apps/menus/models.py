from django.db import models

from utils.models.base_models import BaseModel


class Menu(BaseModel):
    userId = models.CharField('用户ID', primary_key=True, max_length=10, help_text='用户ID')
    userName = models.CharField('用户名称', max_length=200, help_text='用户名称')
    roleId = models.CharField('角色ID', max_length=10, help_text='角色ID')
    content = models.TextField('菜单明细', help_text='菜单明细')

    class Meta:
        db_table = 'menu_info'
        verbose_name = '菜单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userName
