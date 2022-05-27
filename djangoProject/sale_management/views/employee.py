from sale_management.models import Employee
from django.views import generic


class DetailView(generic.DetailView):
    model = Employee
    template_name = 'sale_management/employee/detail.html'


class ListingView(generic.ListView):
    template_name = 'sale_management/employee/index.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.order_by('id')

