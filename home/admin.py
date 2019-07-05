from django.contrib import admin
from .models import News,Tdk
# Register your models here.
# admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ['title', 'url', 'create_time']

    '''每页显示条目数'''
    list_per_page = 20

    '''按发布日期排序'''
    ordering = ('-create_time',)


@admin.register(Tdk)
class NewsAdmin(admin.ModelAdmin):

    '''设置列表可显示的字段'''
    list_display = ['title', 'description', 'keyword']

    '''每页显示条目数'''
    list_per_page = 20

    '''按发布日期排序'''
    ordering = ('-create_time',)