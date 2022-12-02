# Generated by Django 4.1.3 on 2022-12-02 08:23

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(error_messages={'unique': '手机号已存在'}, help_text='手机号', max_length=11, validators=[utils.validators.MobileValidator()], verbose_name='mobile'),
        ),
    ]
