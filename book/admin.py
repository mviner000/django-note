from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'controlno', 'title', 'author_code')
    search_fields = ('id', 'controlno', 'title')
    list_filter = ('author_code',)
    readonly_fields = ('thumbnail_url',)
    ordering = ('id',)

    def thumbnail_url(self, obj):
        if obj.thumbnail:
            return f'<img src="{obj.thumbnail.url}" width="100" height="100">'
        else:
            return '(No thumbnail)'

    thumbnail_url.allow_tags = True
    thumbnail_url.short_description = 'Thumbnail'

admin.site.register(Book, BookAdmin)
