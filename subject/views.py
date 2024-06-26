from rest_framework import viewsets, serializers, pagination
from rest_framework.response import Response
from book.models import Book
from book.serializers import BookSerializer
from .serializers import TopSubjectsSerializer
from rest_framework import generics
from .models import Subject
from .serializers import SubjectSerializer

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

class TopSubjectsViewSet(viewsets.ViewSet):
    def list(self, request):
        # Calculate the number of books per subject
        subjects_books_count = {}

        books = Book.objects.select_related('subject1_code').all()

        for book in books:
            subject_id = book.subject1_code.id  # Assuming 'id' is the subject's unique identifier
            subject_name = book.subject1_code.subject_name
            if subject_name not in subjects_books_count:
                subjects_books_count[subject_name] = {
                    'id': subject_id,
                    'count': 0
                }
            subjects_books_count[subject_name]['count'] += 1

        # Sort subjects by the number of books in descending order
        sorted_subjects = sorted(subjects_books_count.items(), key=lambda x: x[1]['count'], reverse=True)

        # Get top 10 subjects (or less if less than 10 subjects exist)
        top_subjects = sorted_subjects[:10]

        # Serialize the top subjects
        serialized_data = []
        for subject_name, data in top_subjects:
            serializer = TopSubjectsSerializer({
                'id': data['id'],
                'subject_name': subject_name,
                'book_count': data['count']
            })
            serialized_data.append(serializer.data)

        return Response(serialized_data)
    
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Fetch related books for the subject
        books = instance.books_subject1.all()  # Use the related_name 'books_subject1' here
        book_serializer = BookSerializer(books, many=True)

        # Append books data to the subject serializer response
        data = serializer.data
        data['books'] = book_serializer.data

        return Response(data)
