from django.shortcuts import render
from django.views import View
from .models import User, Product, Order

class CustomerOrdersView(View):
    template_name = 'myapp2/customer_orders.html'

    def get(self, request, customer_id):
        customer = User.objects.get(pk=customer_id)
        orders = customer.order_set.all()  # все заказы клиента

        context = {'customer': customer, 'orders': orders}
        return render(request, 'myapp2/customer_orders.html', context)


