from rest_framework import serializers
import logging
from .models import Book
from author.models import Author
from subject.models import Subject

logger = logging.getLogger(__name__)

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    def get_author_name(self, obj: Book) -> str:
        return obj.author_code.author_name

    def get_subject_name(self, obj: Book) -> str:
        try:
            return obj.subject1_code.subject_name
        except Subject.DoesNotExist:
            logger.warning(f"Subject matching query does not exist for book control no: {obj.controlno}")
            return None

    def get_thumbnail_url(self, obj: Book) -> str:
        if obj.thumbnail_url:
            # Remove the "image/upload/" part from the URL
            return obj.thumbnail_url.url.replace("image/upload/", "", 1)
        return None

    class Meta:
        model = Book
        fields = ['controlno', 'id', 'title', 'copyright',  'author_code', 'author_name', 'subject1_code', 'subject_name', 'thumbnail_url', 'publisher', 'pubplace', 'pagination', 'edition', 'views', 'stock_quantity']


class BookListSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj: Book) -> str:
        return obj.author_code.author_name

    def get_thumbnail_url(self, obj: Book) -> str:
        if obj.thumbnail_url:
            # Remove the "image/upload/" part from the URL
            return obj.thumbnail_url.url.replace("image/upload/", "", 1)
        return None

    class Meta:
        model = Book
        fields = ['id', 'controlno', 'author_name', 'title', 'thumbnail_url']