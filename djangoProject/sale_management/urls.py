from django.urls import path
from sale_management.views import test, homepage, about, detail, listing


urlpatterns = [
    path('test', test, name='test'),
    path('', homepage, name='homepage'),
    path('about', about, name='about'),
    path('employee/<int:employee_id>/', detail, name='detail'),
    path('employee/', listing, name='listing')
]
