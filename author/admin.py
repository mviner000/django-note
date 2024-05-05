from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_code')  # Display these fields in the admin list
    search_fields = ('author_name', 'author_code')  # Enable search on these fields
    list_filter = ('author_name',)  # Add filters based on these fields
    ordering = ('id',)

    def display_books(self, obj):
        books = obj.books.all()
        return ', '.join([book.title for book in books])


admin.site.register(Author, AuthorAdmin)
