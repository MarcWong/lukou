import json
from lukou import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import News,Tdk
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(reuqest):
    news_count = News.objects.count()
    tdk_data = Tdk.objects.all().first()

    return render(reuqest, 'main.html', {'count':news_count, 'title':tdk_data.title, 'description':tdk_data.description, 'keyword':tdk_data.keyword})

@csrf_exempt
def news(request):

    try:
        curpage = int(request.POST.get('pageIndex', '1'))
        pagesize = int(request.POST.get('pageSize', '1'))
        year = request.POST.get('year','2018')

    except ValueError:
        curpage = 1

    startPos = (curpage - 1) * pagesize
    endPos = startPos + pagesize
    news_data = News.objects.filter(time__year=year).all()[startPos:endPos]
    json_list = []
    for item in news_data:
        print(item)
        json_dict = {}
        json_dict["title"] = item.title
        json_dict["digest"] = item.digest
        json_dict["img"] = str(item.img)
        json_dict["url"] = item.url
        json_dict["time"] = str(item.time.strftime("%Y-%m-%d"))
        json_list.append(json_dict)
    # print(json_list)
    return HttpResponse(json.dumps(json_list), content_type="application/json")

