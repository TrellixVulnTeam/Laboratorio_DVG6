from django.contrib import admin
from .models import Order, OrderDetail, Receipt
# Register your models here.

class OrderDetailInline(admin.TabularInline):
    '''Tabular Inline View for OrderDetail'''

    model = OrderDetail
    extra =0


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    '''Admin View for Receipt'''

    list_display = ('receipt_number','client', 'order','date','total', 'payment')
    ordering = ('receipt_number','date',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ['id', 'date', 'status', 'total' ]
    inlines = [OrderDetailInline]