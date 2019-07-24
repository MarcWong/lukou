from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
# Create your models here.

class News(models.Model):
    '''
        新闻
    '''
    title = models.CharField(max_length=128, verbose_name='标题')
    digest = models.TextField(verbose_name='摘要')
    img = models.ImageField(upload_to='imgs', verbose_name='图片')
    url = models.CharField(max_length=128, verbose_name='链接地址')
    time = models.DateTimeField(default=timezone.now, verbose_name='日期')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    description = models.CharField(max_length=128, verbose_name='描述', default='')
    keyword = models.CharField(max_length=128, verbose_name='关键词', default='')
    content = MDTextField(verbose_name='内容', default='')

    class Meta:
        verbose_name_plural='新闻'


class Tdk(models.Model):
    '''
        网站设置
    '''
    title = models.CharField(max_length=128, verbose_name='标题')
    description = models.CharField(max_length=128, verbose_name='描述')
    keyword = models.CharField(max_length=128, verbose_name='关键词')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural='网站设置'