from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import api_view

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/list/', api_view, name='api'),
]