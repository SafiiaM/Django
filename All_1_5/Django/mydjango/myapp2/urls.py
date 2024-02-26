from django.urls import path
from .views import CustomerOrdersView

urlpatterns = [
    path('customer_orders/<int:customer_id>/', CustomerOrdersView.as_view(), name='customer_orders'),
]

