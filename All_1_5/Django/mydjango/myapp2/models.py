from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, default='')
    address = models.TextField(default='')
    registration_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'name: {self.name}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    added_date = models.DateField(default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'name: {self.name}, price: {self.price}, description: {self.description}'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateField(default=timezone.now, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['customer']

    def __str__(self):
        return f'Order #{self.pk} - {self.customer.name}'

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}' 
    
    # метод "get_summary" возвращает первые 12 слов контента поста и добавляет многоточие в конце.

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'      