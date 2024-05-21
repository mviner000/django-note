from rest_framework import serializers
from .models import Author
from book.models import Book

class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'thumbnail_url']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        thumbnail_url = representation.get('thumbnail_url', '')
        if thumbnail_url and thumbnail_url.startswith('image/upload/'):
            # Remove the prefix "image/upload/"
            representation['thumbnail_url'] = thumbnail_url.replace('image/upload/', '', 1)
        return representation

class AuthorSerializer(serializers.ModelSerializer):
    books = SimpleBookSerializer(many=True, read_only=True)
    book_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'author_name', 'author_code', 'books', 'book_count']  # Include desired fields in the API response
