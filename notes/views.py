from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Create your views here.
class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer