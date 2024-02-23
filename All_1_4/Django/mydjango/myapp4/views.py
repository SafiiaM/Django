from django.shortcuts import render, redirect
import logging
from django.views import View
from .models import Client, Order, Product
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed! Redirect to /lastday/0/7')
    return redirect("/lastday/0/7")


class LastDay(View):
    def get(self, request,  *args, **kwargs):
        client_id = kwargs.get('client_id', 0)
        days = kwargs.get('days', 1)
        
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
        return render(request, 'myapp4/orders.html', context)


class ProductView(View):
    def get(self, request):
        client_id = 1 
        form = ProductForm(initial={'id': '0', 'name': '', 'description': '', 'price': 0, 'amount': 1, 'client_id': client_id})
        message = 'Заполните форму'
        return render(request, 'myapp4/product.html', {'form': form, 'message': message})

    def post(self, request):
        if 'product_id' in request.POST:
            product = Product.objects.filter(pk=request.POST['product_id']).first()
            initial = {'id': str(request.POST['product_id']),
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'amount': product.amount,
                    'image': product.image,
                    }
            form = ProductForm(initial=initial)
            message = 'Измените данные'
            return render(request, 'myapp4/product.html', {'form': form, 'message': message})
        else:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product_id = form.cleaned_data['id']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                price = form.cleaned_data['price']
                amount = form.cleaned_data['amount']
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                logger.info(f'Image: {image.name=}')
                fs.save(image.name, image)

                if product_id == 0:
                    product = Product(name=name, description=description,
                                    price=str(price), amount=amount, image=image.name)
                else:
                    product = Product.objects.filter(pk=product_id).first()
                    product.name = name
                    product.description = description
                    product.price = price
                    product.amount = amount
                    product.image = image.name
                product.save()
                # logger.info(f'Successfully create product: {product}')
                return redirect('lastday', client_id=client_id, days=7)
            else:
                message = 'Ошибка в данных'
                return render(request, 'myapp4/product.html', {'form': form, 'message': message})

