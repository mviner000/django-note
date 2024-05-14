"""
URL configuration for note project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include 
from notes.views import index
from book.views import book_list
from django.conf.urls.static import static

urlpatterns = [
    path('index', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('api/', include('book.urls')),
    path('api/', include('author.urls')),
    path('api/', include('subject.urls')),
    path('api/', include('bookcart.urls')),
    path('api/', include('shop.urls')),
    path('api/', include('product.urls')),
    # Add a direct route to the book list page
    path('', book_list, name='book_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)