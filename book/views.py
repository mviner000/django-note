from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import os
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Book
from .serializers import BookSerializer
import logging
logger = logging.getLogger('note')

from django.db.models import F
from rest_framework.response import Response

from rest_framework import status

class BookPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    cursor_query_param = 'cursor'

    def paginate_queryset(self, queryset, request, view=None):
        cursor = request.query_params.get('cursor')
        if cursor:
            queryset = queryset.filter(id__gt=cursor)
        return super().paginate_queryset(queryset, request, view)
        

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author_code', 'subject1_code').all().order_by('id')
    serializer_class = BookSerializer
    pagination_class = BookPagination

    def list(self, request):
        cursor = request.query_params.get('cursor')
        if cursor:
            queryset = self.queryset.filter(id__gt=cursor)
        else:
            queryset = self.queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def search(self, request):
        query = request.query_params.get('q')
        if query:
            books = Book.objects.filter(
                Q(title__icontains=query) |
                Q(author_code__author_name__icontains=query) |
                Q(subject1_code__subject_name__icontains=query)
            )
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        return Response([])
    
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.views += 1
        book.save()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Book.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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