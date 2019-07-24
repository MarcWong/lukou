import json
from lukou import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import News,Tdk
from django.views.decorators.csrf import csrf_exempt
import markdown
# Create your views here.


def index(request):
    news_count = News.objects.count()
    tdk_data = Tdk.objects.all().first()

    return render(request, 'main.html', {'count':news_count, 'title':tdk_data.title, 'description':tdk_data.description, 'keyword':tdk_data.keyword})

@csrf_exempt
def news(request):

    try:
        curpage = int(request.POST.get('pageIndex', '1'))
        pagesize = int(request.POST.get('pageSize', '5'))
        year = request.POST.get('year','2019')

    except ValueError:
        curpage = 1

    startPos = (curpage - 1) * pagesize
    endPos = startPos + pagesize

    news_data = News.objects.filter(time__year=year).all()[startPos:endPos]
    print(news_data)
    json_list = []
    for item in news_data:
        print(item)
        json_dict = {}
        json_dict["title"] = item.title
        json_dict["id"] = item.id
        json_dict["digest"] = item.digest
        json_dict["img"] = str(item.img)
        json_dict["url"] = item.url
        json_dict["time"] = str(item.time.strftime("%Y-%m-%d"))
        json_list.append(json_dict)
    # print(json_list)
    return render(request, 'news.html', {"res":json_list})
    # return HttpResponse(json.dumps(json_list), content_type="application/json")

def new_markdown(request):
    id = request.GET['id']
    news_data = News.objects.filter(id=id).first()
    content = markdown.markdown(news_data.content)
    return render(request, 'news_md.html', {"content":content})
