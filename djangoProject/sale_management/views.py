# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# # from django.template import loader
# from sale_management.models import Employee, Customer, Product, Order, OrderDetail
# from django.views import generic
#
# # Create your views here.
#
#
# def frontpage(request):
#     return render(request, 'front_page.html')
#
#
# def homepage(request):
#     return render(request, 'homepage.html')
#
#
# def about(request):
#     return render(request, 'about.html')
#
#
# # def employee_detail(request, employee_id):
# #     # try:
# #     #     employee = Employee.objects.get(pk=employee_id)
# #     # except Employee.DoesNotExist:
# #     #     raise Http404("Employee does not exist")
# #     # return HttpResponse(employee)
# ##
# #     employee = get_object_or_404(Employee, pk=employee_id)
# #     return render(request, 'sale_management/employee/detail.html', {'employee': employee})
#

#
#
# # def employee_listing(request):
# #     latest_employee_list = Employee.objects.order_by('-created_at')[:5]
# #     latest_employee = {
# #         'latest_employee_list': latest_employee_list
# #     }
#
#     # template = loader.get_template('sale_management/employee/index.html')
#     # output = ', '.join([e.name for e in latest_employee_list])
#     # return HttpResponse(template.render(context, request))
#     # return render(request, 'sale_management/employee/index.html', latest_employee)
#
#
# def customer_detail(request, customer_id):
#     customer = get_object_or_404(Customer, pk=customer_id)
#     return render(request, 'sale_management/customer/detail.html', {'customer': customer})
#
#
# def customer_listing(request):
#     latest_customer_list = Customer.objects.order_by('-created_at')[:5]
#     latest_customer = {
#         'latest_customer_list': latest_customer_list
#     }
#
#     return render(request, 'sale_management/customer/index.html', latest_customer)
#
#

# # def product_detail(request, product_id):
# #     product = get_object_or_404(Product, pk=product_id)
# #     return render(request, 'sale_management/product/detail.html', {'product': product})
# #
# #
# # def product_listing(request):
# #     product_list = Product.objects.order_by('id')
# #     product = {
# #         'product_list': product_list
# #     }
# #
# #     return render(request, 'sale_management/product/index.html', product)
#
#
# def order_detail(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     order_details = OrderDetail.objects.filter(order_id=order_id)
#     return render(request, 'sale_management/order/detail.html', {'order': order, 'order_details': order_details})
#
#
# def order_listing(request):
#     order_list = Order.objects.order_by('id')
#     order = {
#         'order_list': order_list
#     }
#
#     return render(request, 'sale_management/order/index.html', order)
