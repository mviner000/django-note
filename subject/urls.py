from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BooksBySubjectViewSet, TopSubjectsViewSet
from .views import SubjectDetailView

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'subjects', BooksBySubjectViewSet, basename='books_by_subject')

# Define a new endpoint for top subjects
top_subjects_router = DefaultRouter()
top_subjects_router.register(r'subjects/top', TopSubjectsViewSet, basename='top_subjects')

# The API URLs are now determined automatically by the routers
urlpatterns = [
    path('', include(router.urls)),
    path('', include(top_subjects_router.urls)),  # Add the new URL endpoint for top subjects
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
]
