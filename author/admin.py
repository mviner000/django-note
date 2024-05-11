from django.contrib import admin
from .models import Author
from book.models import Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    
    # Specify the foreign key relationship to use (choose one based on your model design)
    fk_name = 'author_code'  # This should match the name of the ForeignKey field in the Book model

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_code', 'display_books')
    search_fields = ('author_name', 'author_code')
    list_filter = ('author_name',)
    ordering = ('id',)
    inlines = [BookInline]

    def display_books(self, obj):
        books = obj.books.all()
        book_titles = ', '.join([book.title for book in books])
        return book_titles
    
    display_books.short_description = 'Books by this Author'

admin.site.register(Author, AuthorAdmin)
