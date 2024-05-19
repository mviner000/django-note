from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from .models import BookCart
from rest_framework.permissions import AllowAny
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

        # Check if the borrowing is being verified
        if request.data.get('is_borrowed_verified', False):
            for book in instance.books.all():
                book.stock_quantity -= 1
                book.save()
                
        serializer.save()
        return Response(serializer.data)
    
    @action(methods=['patch'], detail=True, permission_classes=[AllowAny])
    def verify_return(self, request, pk=None):
        book_cart = self.get_object()
        book_cart.is_returned_verified = True
        book_cart.save()

        for book in book_cart.books.all():
            book.stock_quantity += 1
            book.save()

        return Response({'message': 'Return verification successful'})

class BookCartListViewSet(viewsets.ModelViewSet):
    queryset = BookCart.objects.filter(is_borrowed_verified=False)  # Filter BookCarts by is_borrowed_verified
    serializer_class = BookCartSerializer
    permission_classes = [permissions.AllowAny]