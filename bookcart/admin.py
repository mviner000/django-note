from django.contrib import admin
from .models import BookCart

class BookCartAdmin(admin.ModelAdmin):
    list_display = ('student', 'books_display', 'is_borrowed_verified', 'is_returned_verified', 'created_at', 'updated_at')
    list_filter = ('is_borrowed_verified', 'is_returned_verified')
    search_fields = ('student',)
    ordering = ('-updated_at',)

    def books_display(self, obj):
        return ', '.join(book.title for book in obj.books.all())
    books_display.short_description = 'Books'

admin.site.register(BookCart, BookCartAdmin)