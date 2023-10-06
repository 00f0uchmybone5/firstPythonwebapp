from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, ("/home/ty/mysite/home/index.html"))

# Create your views here.
