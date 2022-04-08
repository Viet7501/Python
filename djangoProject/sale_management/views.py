from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    return HttpResponse('Hello, this is a test run!')


def test(request):
    return HttpResponse('This is working properly!')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')

def home(request):
    return HttpResponse('Home page')
