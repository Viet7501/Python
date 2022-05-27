from django.contrib import admin
from django.utils import timezone
# Register your models here.
from .models import Employee, Customer, Product, Order, OrderDetail


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {
            'fields': ['name', 'dob', 'gender']
        }),
        ('Address', {
            'fields': ['address']
        }),
    ]

    list_display = ['id', 'name', 'address', 'was_employee_birthday_today', 'employee_age', 'gender']
    list_display_links = ['id', 'name']

    def was_employee_birthday_today(self, obj):
        today = timezone.now().date()
        return (obj.dob.month, obj.dob.day) == (today.month, today.day)
    was_employee_birthday_today.boolean = True

    def employee_age(self, obj):
        today = timezone.now()
        return today.year - obj.dob.year - ((today.month, today.day) < (obj.dob.month, obj.dob.day))


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {
            'fields': ['name', 'contact_name', 'contact_number']
        }),
        ('Address', {
            'fields': ['address']
        }),
    ]

    list_display = ['id', 'contact_name', 'contact_number', 'address']
    list_display_links = ['id', 'contact_name']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {
            'fields': ['name']
        }),
        ('Price', {
            'fields': ['price']
        }),
        ('Available', {
            'fields': ['quantity']
        }),
    ]

    list_display = ['id', 'name', 'price', 'quantity']
    list_display_links = ['id', 'name']


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0
    fields = ['product', 'quantity', 'price']


class OrderAdmin(admin.ModelAdmin):
    # fields = ['customer', 'employee', 'status', 'deliver_date']
    fieldsets = [
        ('Customer, Employee Information', {
            'fields': ['customer', 'employee']
        }),
        ('Status', {
            'fields': ['status']
        }),
        ('Date Information', {
            'fields': ['deliver_date']
        }),
    ]

    list_display = ['id', 'customer', 'employee', 'status', 'purchase_date', 'total', 'was_delivered']
    list_display_links = ['id', 'customer', 'employee']

    inlines = [OrderDetailInline]

    def total(self, obj):
        total = 0
        for order_detail in obj.orderdetail_set.all():
            total += order_detail.subtotal
        return total

    def was_delivered(self, obj):
        time_now = timezone.now().date()
        return obj.deliver_date < time_now
    was_delivered.boolean = True


class OrderDetailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Order id, Product', {
            'fields': ['order', 'product']
        }),
        ('Quantity, Price', {
            'fields': ['quantity', 'price']
        }),

    ]

    list_display = ['id', 'order', 'product', 'price', 'quantity', 'subtotal']
    list_display_links = ['id', 'order']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)
