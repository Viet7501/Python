from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    return HttpResponse('Hello, this is a test run!')


def test(request):
    return HttpResponse('This is working properly!')


def display_meta(request):
    values = request.META.items()
    values.sort
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '/n'.join(html))
