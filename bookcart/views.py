from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from .models import BookCart
from rest_framework import permissions 
from .serializers import BookCartSerializer
from rest_framework.response import Response

class BookCartViewSet(viewsets.ModelViewSet):
    queryset = BookCart.objects.all()
    serializer_class = BookCartSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BookCartListViewSet(viewsets.ModelViewSet):
    queryset = BookCart.objects.filter(is_borrowed_verified=False)  # Filter BookCarts by is_borrowed_verified
    serializer_class = BookCartSerializer
    permission_classes = [permissions.AllowAny]