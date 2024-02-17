from django.core.management.base import BaseCommand

from myapp2.models import Order
from myapp2.models import Product
from myapp2.models import User

class Command(BaseCommand):
    help = "Create order. Inter id user and id product"

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            user = User.objects.get(id=i)
            for i in range(1, 5):
                product1 = Product.objects.get(id=i+104)
                product2 = Product.objects.get(id=i+105)
                self.stdout.write(f'{user}')
                self.stdout.write(f'{product1}')
                self.stdout.write(f'{product2}')
                order = Order(customer=user, total_price=4+i)
                order.save()
                order.products.add(product1)
                order.products.add(product2)
                order.save()
                self.stdout.write(f'{order}')