from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=150, null=True)
    age = models.IntegerField()
    date_reg = models.DateTimeField(default=timezone.now) #auto_now_add=True
    # is_deleted = BooleanField(default=False)  

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    # image = models.ImageField(upload_to='products/')
    count_product = models.DecimalField(max_digits=30, decimal_places=3, default=0.0)
    date_add = models.DateTimeField(default=timezone.now) #auto_now_add=True
    # is_deleted = BooleanField(default=False)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return f'name: {self.name}, price: {self.price}, description: {self.description}'
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Product) 
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    # is_deleted = BooleanField(default=False) 
    class Meta:
        ordering = ['customer']

    def __str__(self):
        return f'customer: {self.customer}, product: {self.products}, price: {self.total_price}'


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