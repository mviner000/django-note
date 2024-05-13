from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookCartViewSet, BookCartListViewSet

router = DefaultRouter()
router.register(r'bookcarts', BookCartViewSet)
router.register(r'unverified-bookcarts', BookCartListViewSet, basename='unverified-bookcarts')  # Register new BookCartListViewSet


urlpatterns = [
    path('', include(router.urls)),
]
