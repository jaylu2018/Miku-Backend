# Generated by Django 4.1.3 on 2022-12-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0006_remove_dept_pid_dept_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='child',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='描述'),
        ),
    ]
