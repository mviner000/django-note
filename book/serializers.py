from rest_framework import serializers
import logging
from .models import Book
from author.models import Author
from subject.models import Subject


logger = logging.getLogger(__name__)

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author_code.author_name
    
    def get_subject_name(self, obj):
        try:
            return obj.subject1_code.subject_name
        except Subject.DoesNotExist:
            logger.warning(f"!!!!!PLEASE FIX! \nSubject matching query does not exist for book control no: {obj.controlno} \n--------")
            return None  # or return a default value

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_code', 'author_name', 'subject1_code', 'subject_name']  # Update fields to include 'author_name'
