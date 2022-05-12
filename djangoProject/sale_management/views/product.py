from sale_management.models import Product
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.db.models import Q


class DetailView(generic.DetailView):
    model = Product
    template_name = 'sale_management/product/detail.html'


class ListingView(generic.ListView):
    template_name = 'sale_management/product/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.order_by('id')


def update_price(request, product_id):
    try:
        price = float(request.POST['price'])
        if price > 0:
            affected_rows = Product.objects.filter(id=product_id).filter(~Q(price=price)).update(price=price)
            if affected_rows == 1:
                message = "Updated is successfully"
            else:
                message = "Price is not changed"
        else:
            message = "Price must be greater than 0"
    except (KeyError, ValueError):
        message = "Invalid input"

    product = get_object_or_404(Product, pk=product_id)
    return render(
        request,
        'sale_management/product/detail.html',
        {
            'product': product,
            'message': message
        }
    )
