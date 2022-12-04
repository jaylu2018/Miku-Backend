# Generated by Django 4.1.3 on 2022-12-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='是否为admin', verbose_name='是否为admin'),
        ),
        migrations.AddField(
            model_name='role',
            name='status',
            field=models.BooleanField(default=True, help_text='角色状态', verbose_name='角色状态'),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='角色名称'),
        ),
    ]
