from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksBySubjectViewSet

# Create a router and register the AuthorViewSet
router = DefaultRouter()
router.register(r'subjects', BooksBySubjectViewSet, basename='books_by_subject')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
