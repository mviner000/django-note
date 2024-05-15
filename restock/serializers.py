from rest_framework import serializers
from .models import Restock

class RestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restock
        fields = ['id', 'product', 'restocker_id', 'timestamp', 'old_quantity', 'new_quantity']
        read_only_fields = ['id', 'timestamp', 'old_quantity']

    def create(self, validated_data):
        product = validated_data['product']
        new_quantity = validated_data['new_quantity']

        old_quantity = product.stock_quantity
        product.stock_quantity += new_quantity
        product.save()

        restock = Restock.objects.create(
            product=product,
            restocker_id=validated_data['restocker_id'],
            old_quantity=old_quantity,
            new_quantity=new_quantity
        )
        return restock
