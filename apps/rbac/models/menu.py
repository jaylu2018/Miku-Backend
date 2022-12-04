from django.db import models


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")
    icon = models.CharField(max_length=50, null=True, blank=True, verbose_name="图标")
    path = models.CharField(max_length=158, null=True, blank=True, verbose_name="链接地址")
    is_frame = models.BooleanField(default=False, verbose_name="外部菜单")
    is_show = models.BooleanField(default=True, verbose_name="显示标记")
    sort = models.IntegerField(null=True, blank=True, verbose_name="排序标记")
    component = models.CharField(max_length=200, null=True, blank=True, verbose_name="组件")
    pid = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['id']
