from sale_management.models import Order
from django.views import generic
from django.shortcuts import get_object_or_404, render
from sale_management.constants import OrderStatus

# Pdf
from djangoProject import settings
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os


class DetailView(generic.DetailView):
    model = Order
    template_name = 'sale_management/order/detail.html'


class ListingView(generic.ListView):
    template_name = 'sale_management/order/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.order_by('id')


def _previous_status(order):
    message = ''
    pre_status = order.status

    if order.status == OrderStatus.STATUS_ACCEPTED:
        pre_status = OrderStatus.STATUS_NEW
    else:
        message = 'Dont have previous status'

    return pre_status, message


def _next_status(order):
    message = ''
    next_status = order.status

    if order.status == OrderStatus.STATUS_NEW:
        next_status = OrderStatus.STATUS_ACCEPTED
    else:
        message = 'Dont have previous status'

    return next_status, message


def update_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    if 'previous' in request.POST:
        pre_status, message = _previous_status(order)
        if not message:
            order.status = pre_status
            order.save()
    elif 'next' in request.POST:
        next_status, message = _next_status(order)
        if not message:
            order.status = next_status
            order.save()
    else:
        message = 'Invalid action'

    order = get_object_or_404(Order, pk=order_id)
    return render(
        request,
        'sale_management/order/detail.html',
        {
            'order': order,
            'message': message
        }
    )


def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)  # , link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
