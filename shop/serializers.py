from rest_framework import serializers
from product.serializers import ProductSerializer  # Import the ProductSerializer
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Nested serialization for products

    class Meta:
        model = Shop
        fields = ['id', 'name', 'owner', 'address', 'email', 'phone', 'products', 'created_at', 'updated_at']
