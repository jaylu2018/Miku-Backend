# Generated by Django 4.1.3 on 2022-12-07 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0008_rename_child_dept_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dept',
            name='children',
        ),
    ]