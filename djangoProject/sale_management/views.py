from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):

    return HttpResponse('Hello, this is a test run!')


def test(request):
    return HttpResponse('This is working properly!')


def frontpage(request):
    return render(request, 'front_page.html')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')

