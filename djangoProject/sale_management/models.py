from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    dob = models.DateField(null=True)  # date of birth

    def __str__(self):
        return f'{self.id} - {self.name}'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.contact_number}'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.name} - {self.price}'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    purchase_at = models.DateTimeField()
    deliver_at = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id} - {self.purchase_at} - {self.deliver_at}'


class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.order} - {self.product} - {self.quantity}'
