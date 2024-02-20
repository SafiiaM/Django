from django.shortcuts import render, redirect
from django.views import View
#from django.http import HttpResponse, JsonResponse 
from .models import Client, Order
from django.utils import timezone
from datetime import datetime, timedelta


def index(request):
    return render(request, 'myapp3/orders.html')



class LastDay(View):
    def get(self, request, client_id, days=1):
        if client_id == 0:
            try:
                client_id = list(Client.objects.values_list('id', flat=True))[0]
            except IndexError:
                client_id = None

        orders = ((Order.objects
                .filter(client_id=client_id, order_date__gte=datetime.now(tz=timezone.utc) - timedelta(days=days)))
                .distinct()
                .order_by("order_date")
                )

        context = {'orders': orders,
                'client_id': client_id,
                'clients': Client.objects.all(),
                'days': days,
                }
        return render(request, 'myapp3/orders.html', context)
