from django.db import models
from django.utils import timezone


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=30)
    address = models.TextField(max_length=150)
    register_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.name}: зарегистрирован - {self.register_date}'


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=1)
    image = models.ImageField(max_length=255, upload_to='Django\mydjango\mydjango\media')
    create_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.name}: цена - {self.price}'



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'Клиент: {self.client}, общая сумма заказа: {self.total_price}, дата оформления:' \
            f' {self.order_date}'
