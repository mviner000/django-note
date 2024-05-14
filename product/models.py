from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    barcode = models.CharField(max_length=255)
    grocery_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    image = CloudinaryField('image', folder='products')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
