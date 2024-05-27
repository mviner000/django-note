from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import api_view, book_detail
from .views import SearchBooksAPI

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/search/', SearchBooksAPI.as_view(), name='book_search'),
    path('books/all/', BookViewSet.as_view({'get': 'all_books'}), name='all_books'),
    path('', include(router.urls)),
    path('books/list/', api_view, name='api'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('books/search/', BookViewSet.as_view({'get': 'search'}), name='book_search'),
]