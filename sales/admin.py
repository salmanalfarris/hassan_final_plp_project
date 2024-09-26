from django.contrib import admin
from .models import Customer, Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('customer__name', 'product__name')

admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)

# #Login credentials to my django admin super user account
# Username: Salmanalfarris
# Password: H3491675846h@