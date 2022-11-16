from django.db import models

from utils.models.base_models import BaseModel


class Interfaces(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('接口名称', max_length=200, unique=True, help_text='接口名称')
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE,
                                related_name='interfaces', help_text='所属项目')
    desc = models.CharField('简要描述', max_length=200, null=True, blank=True, help_text='简要描述')

    class Meta:
        db_table = 'interfaces_info'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
