import json
from lukou import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import News,Tdk
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
# Create your views here.


def index(request):
    news_count = News.objects.count()
    tdk_data = Tdk.objects.all().first()

    return render(request, 'main.html', {'count':news_count, 'title':tdk_data.title, 'description':tdk_data.description, 'keyword':tdk_data.keyword})

@csrf_exempt
def news(request):

    year = request.GET.get('years','2019')

    news_data = News.objects.filter(time__year=year).all().order_by('-update_time')
    paginator = Paginator(news_data, 2)
    page_num = request.GET.get('page', 1)  # 获取url的页码参数。GET返回字典，page_num默认为1
    page_of_blogs = paginator.get_page(page_num)
    print(page_of_blogs)
    current_page_num = page_of_blogs.number  # 获取当前页码
    # 获取前后各页
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
        range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    #  加上首尾页码
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['res'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range

    return render(request, 'news.html', context)
    # return render(request, 'news.html', {"res":json_list,'page_range': page_range})

def new_markdown(request):
    id = request.GET['id']
    news_data = News.objects.filter(id=id).first()
    content = markdown.markdown(news_data.content)
    return render(request, 'news_md.html', {"content":content})
