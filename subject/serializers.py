from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_name', 'temp_id', 'subject_code']

class TopSubjectsSerializer(serializers.Serializer):
    subject_name = serializers.CharField()
    book_count = serializers.IntegerField()
    id = serializers.IntegerField()
