from rest_framework import serializers
from .models import BookCart
from book.models import Book  # Import Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookCartSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)  # Use PrimaryKeyRelatedField for array of book IDs

    class Meta:
        model = BookCart
        fields = '__all__'

    def create(self, validated_data):
        books_data = validated_data.pop('books')  # Separate books data
        book_cart = BookCart.objects.create(**validated_data)  # Create BookCart instance

        # Add books to the BookCart
        book_cart.books.set(books_data)

        return book_cart
