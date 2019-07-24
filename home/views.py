import json
from lukou import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import News,Tdk
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
import markdown
# Create your views here.


def index(request):
    news_count = News.objects.count()
    tdk_data = Tdk.objects.all().first()

    return render(request, 'main.html', {'count':news_count, 'title':tdk_data.title, 'description':tdk_data.description, 'keyword':tdk_data.keyword})

@csrf_exempt
def news(request):

    year = request.GET.get('year','2019')

    news_data = News.objects.filter(time__year=year).all().order_by('-update_time')
    paginator = Paginator(news_data, 10)
    page= request.GET.get('page', 1)  # 获取url的页码参数。GET返回字典，page_num默认为1
    try:
        #通过获取上面的page参数，查询此page是否为整数并且是否可用
        subject_obj = paginator.page(page)
    except PageNotAnInteger:
        subject_obj = paginator.page(1)
    except (EmptyPage, InvalidPage):
        subject_obj = paginator.page(paginator.num_pages)

    page_of_blogs = paginator.get_page(page)

    return render(request, 'news.html', {"res":page_of_blogs.object_list,'subject_list': subject_obj})


def new_markdown(request):
    id = request.GET['id']
    news_data = News.objects.filter(id=id).first()
    content = markdown.markdown(news_data.content)
    return render(request, 'news_md.html', {"content":content, 'title':news_data.title, 'description':news_data.description, 'keyword':news_data.keyword})
