from django.core.management.base import BaseCommand
from myapp2.models import Product
from datetime import datetime

class Command(BaseCommand):
    
    help = "Create product."

    def handle(self, *args, **kwargs):
        for i in range(1, 100):
            product = Product(name=f'butter{i}', price=1.99, description=f"for lunch{i}", count_product=126, date_add = datetime(2024,1,1))
            product.save()
            self.stdout.write(f'{product}')