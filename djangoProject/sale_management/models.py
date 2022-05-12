from django.db import models
from django.contrib.auth.models import User
from sale_management.constants import OrderStatus

# Create your models here.

class CreatedAbstractModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_by'
    )
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modified_by'
    )
    modified_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class TrackingAbstractModel(CreatedAbstractModel, ModifiedAbstractModel):
    class Meta:
        abstract = True


class Employee(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True)  # date of birth

    def __str__(self):
        return f'{self.id} - {self.name}'


class Customer(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.contact_name}'

    def save_name(self):
        self.name = self.name.upper()
        self.save()


class Product(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Order(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    purchase_at = models.DateTimeField(auto_now_add=True)
    deliver_at = models.DateField(null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=OrderStatus.STATUS_NEW, choices=OrderStatus.STATUS_CHOICES)

    def __str__(self):
        return f'{self.id} - {self.customer.contact_name} - {self.purchase_at} - {self.deliver_at}'

    @property
    def status_str(self):
        return OrderStatus.STATUS_CHOICES_DICT.get(self.status)


class OrderDetail(TrackingAbstractModel):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.order} - {self.product} - {self.quantity}'

    @property
    def subtotal(self):
        return self.quantity * self.product.price

