from django.urls import path
from sale_management.views import index, test, homepage, about


urlpatterns = [
    path('index', index, name='index'),
    path('test', test, name='test'),
    path('', homepage, name='homepage'),
    path('about', about, name='about')
]
