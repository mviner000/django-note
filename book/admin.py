from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('controlno', 'title', 'author_code', 'edition', 'publisher', 'thumbnail_url')  # Add 'thumbnail_display' to list_display
    search_fields = ('controlno', 'title', 'author_code__name')  # Assuming 'author_code' has a field named 'name'
    list_filter = ('author_code',)  # Add 'author_code' to list_filter
    readonly_fields = ('thumbnail_url',)  # Make 'thumbnail_url' read-only

    def thumbnail_url(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" width="100" height="100">'
        else:
            return '(No thumbnail)'

    thumbnail_url.allow_tags = True
    thumbnail_url.short_description = 'Thumbnail'

admin.site.register(Book, BookAdmin)
