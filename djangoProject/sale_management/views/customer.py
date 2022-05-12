from django.views import generic
from sale_management.models import Customer


class DetailView(generic.DetailView):
    model = Customer
    template_name = 'sale_management/customer/detail.html'


class ListingView(generic.ListView):
    template_name = 'sale_management/customer/index.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.order_by('id')
