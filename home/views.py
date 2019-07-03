import json
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from .models import News
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(reuqest):
    news_count = News.objects.count()
    return render(reuqest, 'main.html')

@csrf_exempt
def news(request):

    try:
        curPage = int(request.POST.get('pageIndex', '1'))
        pageSize = int(request.POST.get('pageSize', '1'))

    except ValueError:
        curPage = 1

    startPos = (curPage - 1) * pageSize
    endPos = startPos + pageSize
    news_data = News.objects.all()[startPos:endPos]
    json_list = []
    for item in news_data:
        json_dict = {}
        json_dict["title"] = item.title
        json_dict["digest"] = item.digest
        json_dict["img"] = str(item.img)
        json_dict["url"] = item.url
        json_dict["create_time"] = str(item.create_time)
        json_list.append(json_dict)

    return HttpResponse(json.dumps(json_list), content_type="application/json")

