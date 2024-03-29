# Generated by Django 4.1.3 on 2022-12-05 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_dept'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dept',
            options={'verbose_name': '部门表', 'verbose_name_plural': '部门表'},
        ),
        migrations.AddField(
            model_name='dept',
            name='email',
            field=models.EmailField(blank=True, help_text='邮箱', max_length=32, null=True, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='dept',
            name='owner',
            field=models.CharField(blank=True, help_text='负责人', max_length=32, null=True, verbose_name='负责人'),
        ),
        migrations.AddField(
            model_name='dept',
            name='phone',
            field=models.CharField(blank=True, help_text='联系电话', max_length=32, null=True, verbose_name='联系电话'),
        ),
        migrations.AddField(
            model_name='dept',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.dept', verbose_name='上级部门'),
        ),
        migrations.AddField(
            model_name='dept',
            name='status',
            field=models.BooleanField(blank=True, default=True, help_text='部门状态', null=True, verbose_name='部门状态'),
        ),
        migrations.AddField(
            model_name='dept',
            name='type',
            field=models.CharField(choices=[('company', '公司'), ('department', '部门')], default='department', max_length=20, verbose_name='部门类型'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(max_length=60, verbose_name='部门名称'),
        ),
    ]
