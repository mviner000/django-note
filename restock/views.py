from rest_framework import generics
from .models import Restock
from .serializers import RestockSerializer

class RestockListCreateAPIView(generics.ListCreateAPIView):
    queryset = Restock.objects.all()
    serializer_class = RestockSerializer

class RestockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restock.objects.all()
    serializer_class = RestockSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        new_quantity = serializer.validated_data['new_quantity']
        
        # Adjust the product stock quantity based on the new restock quantity
        instance.product.stock_quantity += (new_quantity - instance.new_quantity)
        instance.product.save()

        serializer.save()
