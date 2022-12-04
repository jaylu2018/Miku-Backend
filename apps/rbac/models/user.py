from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    mobile = models.CharField(max_length=11, default="", verbose_name="手机号码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    image = models.ImageField(upload_to="static/%Y/%m", default="image/default.png",
                              max_length=100, null=True, blank=True)
    department = models.ForeignKey("Organization", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="部门")
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="上级主管")
    roles = models.ManyToManyField("Role", verbose_name="角色", blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username
