from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('controlno', 'title', 'author_code', 'edition', 'publisher')
    search_fields = ('controlno', 'title', 'author_code__author_name')
    list_filter = ('author_code',)

admin.site.register(Book, BookAdmin)