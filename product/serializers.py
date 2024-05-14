from rest_framework import serializers
from cloudinary import CloudinaryImage

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'barcode', 'grocery_price',
                  'selling_price', 'stock_quantity', 'image_url',
                  'available', 'created_at', 'updated_at']

    def get_image_url(self, obj: Product) -> str:
        if obj.image:
            # Remove the "image/upload/" part from the URL
            return obj.image.url.replace("image/upload/", "", 1)
        return None