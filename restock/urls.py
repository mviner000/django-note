# restock/urls.py

from django.urls import path
from .views import RestockListCreateAPIView, RestockRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('restocks/', RestockListCreateAPIView.as_view(), name='restock-list-create'),
    path('restocks/<int:pk>/', RestockRetrieveUpdateDestroyAPIView.as_view(), name='restock-detail')
]
