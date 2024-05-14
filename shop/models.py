from django.db import models
from product.models import Product

class Shop(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    products = models.ManyToManyField(Product, related_name='shops')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name