from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import render
from django.db.models import F
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

# Create your views here.
class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Note.objects.filter(pk=instance.pk).update(views=F('views') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)