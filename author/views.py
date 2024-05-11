from django.db.models import Count
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Author
from .serializers import AuthorSerializer

class AuthorPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.annotate(book_count=Count('books')).order_by('-book_count', 'id')
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
