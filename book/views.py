from django.shortcuts import render, get_object_or_404
import os
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

def book_detail(request, book_id):
    # Retrieve the book object using its ID
    book = get_object_or_404(Book, pk=book_id)

    # Render the book_detail.html template with the book object
    return render(request, 'book_detail.html', {'book': book})

def book_list(request):
    book_list = Book.objects.all().order_by('title')

    paginator = Paginator(book_list, 10)  # Show 10 books per page
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'books': books})