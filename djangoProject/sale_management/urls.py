from django.urls import path
from sale_management.views import index, test

urlpatterns = [
    path('', index, name='index'),
    path('test', test, name='test')
]
