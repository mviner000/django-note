from rest_framework import serializers
from .models import Author
from book.serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'author_name', 'author_code', 'books']  # Include desired fields in the API response
