from django.contrib import admin
from .models import Client, Product, Order

# вывод информации о клиентах на страницах списков

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    ordering = ['name']
    list_filter = ('name', 'phone_number')
    search_fields = ('name',)
    readonly_fields = ['register_date', ]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'phone_number', ],
            },
        ),
        (
            'Contacts',
            {
                'classes': ['collapse', ],
                'fields': ['email', 'address', ],
                'description': 'краткое примечание о наличие или отсутствие задолженности в "address" ',
            },
        ),
        (
            'Reg',
            {
                'classes': ['collapse', ],
                'fields': ['register_date', ],
            },
        ),
    ]

@admin.action(description="Сбросить количество в ноль")
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    ordering = ['amount', '-price']
    list_filter = ['create_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание продукта "description"'
    readonly_fields = ['create_date', ] 
    actions = [reset_amount]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price', 'order_date']
    ordering = ('client',)
    list_filter = ('products',)
    search_fields = ('client',)


# регистрируем модели в админке
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)