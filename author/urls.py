from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

# Create a router and register the AuthorViewSet
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
