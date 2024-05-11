from rest_framework import viewsets, serializers, pagination
from rest_framework.response import Response
from book.models import Book
from book.serializers import BookSerializer

class BooksBySubjectSerializer(serializers.Serializer):
    subject_name = serializers.CharField()
    books = BookSerializer(many=True)

class BooksBySubjectPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BooksBySubjectViewSet(viewsets.ViewSet):
    pagination_class = BooksBySubjectPagination

    def list(self, request):
        # Get all subjects and corresponding books
        subjects = {}
        books = Book.objects.select_related('subject1_code').all()

        for book in books:
            subject_name = book.subject1_code.subject_name
            if subject_name not in subjects:
                subjects[subject_name] = []
            subjects[subject_name].append(book)

        # Paginate the data
        paginator = self.pagination_class()
        paginated_items = list(subjects.items())  # Convert dict_items to a list of tuples
        paginated_data = paginator.paginate_queryset(paginated_items, request)
        
        # Serialize the paginated data
        serialized_data = []
        for subject_name, books_list in paginated_data:
            serializer = BooksBySubjectSerializer({
                'subject_name': subject_name,
                'books': books_list
            })
            serialized_data.append(serializer.data)

        return paginator.get_paginated_response(serialized_data)
