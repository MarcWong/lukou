from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(reuqest):
    return render(reuqest, 'main.html')
