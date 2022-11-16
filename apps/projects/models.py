from django.db import models
from utils.models.base_models import BaseModel


class Projects(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('项目名称', max_length=200, unique=True, help_text='项目名称')
    leader = models.CharField('负责人', max_length=50, help_text='项目负责人')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')

    class Meta:
        db_table = 'projects_info'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



