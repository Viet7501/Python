from django.shortcuts import render

# Create your views here.


def frontpage(request):
    return render(request, 'front_page.html')


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')
