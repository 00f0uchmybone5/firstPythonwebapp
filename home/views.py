from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome home. Please make a choice.")

# Create your views here.
