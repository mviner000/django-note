# restock/models.py

from django.db import models, transaction
from product.models import Product

class Restock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='restocks')
    restocker_id = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    old_quantity = models.PositiveIntegerField(null=True, blank=True)
    new_quantity = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:  # Ensure this is only done on creation
            with transaction.atomic():
                product = self.product
                self.old_quantity = product.stock_quantity
                product.stock_quantity += (self.new_quantity - self.old_quantity)
                product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} restocked by {self.restocker_id} on {self.timestamp}'
