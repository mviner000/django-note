# restock/admin.py

from django.contrib import admin
from .models import Restock
from product.models import Product

class RestockAdmin(admin.ModelAdmin):
    list_display = ('product', 'restocker_id', 'timestamp', 'old_quantity', 'new_quantity')
    search_fields = ('product__name', 'restocker_id')
    list_filter = ('product', 'timestamp')
    readonly_fields = ('timestamp', 'old_quantity', 'new_quantity')

    def save_model(self, request, obj, form, change):
        if not change:  # This is a new instance
            obj.old_quantity = obj.product.stock_quantity
            obj.product.stock_quantity += (obj.new_quantity - obj.old_quantity)
            obj.product.save()
        else:  # This is an update to an existing instance
            previous = Restock.objects.get(pk=obj.pk)
            obj.old_quantity = previous.old_quantity
            if obj.new_quantity != previous.new_quantity:
                obj.product.stock_quantity += (obj.new_quantity - previous.new_quantity)
                obj.product.save()
        super().save_model(request, obj, form, change)

admin.site.register(Restock, RestockAdmin)
