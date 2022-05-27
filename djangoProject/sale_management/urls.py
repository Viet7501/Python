from django.urls import path
from sale_management.views import layout, employee, product, customer, order


urlpatterns = [
    path('', layout.homepage, name='homepage'),

    path('employee/', employee.ListingView.as_view(), name='employee_listing'),
    path('employee/<int:pk>/', employee.DetailView.as_view(), name='employee_detail'),

    path('customer/', customer.ListingView.as_view(), name='customer_listing'),
    path('customer/<int:pk>/', customer.DetailView.as_view(), name='customer_detail'),

    path('product/', product.ListingView.as_view(), name='product_listing'),
    path('product/<int:pk>/', product.DetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/update_price/', product.update_price, name='update_price'),
    path('product/export/', product.export_product, name='export_product'),

    path('order/', order.ListingView.as_view(), name='order_listing'),
    path('order/<int:pk>/', order.DetailView.as_view(), name='order_detail'),
    path('order/<int:order_id>/update_status/', order.update_status, name='update_status'),
    path('order/<int:order_id>/print/', order.print_order, name='print_order'),

]
