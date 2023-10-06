from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(include("/home/ty/mysite/home/index.html"))

# Create your views here.
