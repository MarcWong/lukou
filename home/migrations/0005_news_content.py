# Generated by Django 2.0.1 on 2019-07-23 16:32

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190705_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=mdeditor.fields.MDTextField(default='', verbose_name='内容'),
        ),
    ]
