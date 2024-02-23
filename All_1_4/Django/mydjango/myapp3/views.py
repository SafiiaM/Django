from django.shortcuts import render, redirect
from django.views import View
#from django.http import HttpResponse, JsonResponse 
from .models import Client, Order
from django.utils import timezone
from datetime import datetime, timedelta


def index(request):
    return render(request, 'myapp3/orders.html')


class LastDay(View):
    def get(self, request, client_id):
        if client_id == 0:
            try:
                client_id = Client.objects.values_list('id', flat=True).first()
            except Client.DoesNotExist:
                client_id = None

        end_date = datetime.now(tz=timezone.utc)
        start_date_7 = end_date - timedelta(days=7)
        start_date_30 = end_date - timedelta(days=30)
        start_date_365 = end_date - timedelta(days=365)

        # Получаем уникальные товары за последние 7 дней, 30 дней и 365 дней
        unique_products_7_days = self.get_unique_products(client_id, start_date_7, end_date)
        unique_products_30_days = self.get_unique_products(client_id, start_date_30, end_date)
        unique_products_365_days = self.get_unique_products(client_id, start_date_365, end_date)

        context = {
            'client_id': client_id,
            'clients': Client.objects.all(),
            'unique_products_7_days': unique_products_7_days,
            'unique_products_30_days': unique_products_30_days,
            'unique_products_365_days': unique_products_365_days,
            'show_buttons': False,  # Устанавливаем в False для скрытия кнопок
        }

        return render(request, 'myapp3/orders.html', context)

    def get_unique_products(self, client_id, start_date, end_date):
        orders = Order.objects.filter(client_id=client_id, order_date__gte=start_date, order_date__lte=end_date)
        unique_products = set()

        for order in orders:
            unique_products.update(order.products.all())

        return unique_products


