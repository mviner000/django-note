from django.shortcuts import render
import os
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Book
from .serializers import BookSerializer

class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title') 
    serializer_class = BookSerializer
    pagination_class = BookPagination

def api_view(request):
    # Retrieve HOSTNAME from environment variables
    hostname = os.getenv('HOSTNAME', 'localhost')  # 'localhost' is a fallback default value

    # Render the template with the HOSTNAME variable
    return render(request, 'rest_framework/api.html', {'hostname': hostname})