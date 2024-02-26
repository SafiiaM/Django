from django.contrib import admin
from .models import Author, Post, User, Product, Order
# Register your models here.

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)