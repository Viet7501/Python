from sale_management.models import Order
from django.views import generic
from django.shortcuts import get_object_or_404, render
from sale_management.constants import OrderStatus

import io
from reportlab.pdfgen import canvas
from django.http import FileResponse
from reportlab.lib.units import inch


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


# Generate PDF
def print_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    customer = order.customer
    purchase_date = order.purchase_date
    status = order.status

    buffer = io.BytesIO()  # create a file buffer to receive PDF data
    pdf = canvas.Canvas(buffer)
    pdf.drawCentredString(4.15*inch, 11.3*inch, f'Customer: {customer.name}')
    pdf.drawCentredString(4.15*inch, 10.9*inch, f'Contact name:{customer.contact_name}')
    pdf.drawCentredString(4.15*inch, 10.5*inch, f'Contact number:{customer.contact_number}')
    pdf.drawCentredString(4.15*inch, 10.1*inch, f'Purchase date:{purchase_date}')
    pdf.drawCentredString(4.15*inch, 9.8*inch, f'Status:{status}')

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='order.pdf')
