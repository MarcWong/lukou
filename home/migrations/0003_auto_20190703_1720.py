# Generated by Django 2.0.1 on 2019-07-03 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190703_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 3, 17, 20, 46, 778401), verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='news',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='news',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
    ]