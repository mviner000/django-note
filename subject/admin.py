from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name', 'subject_code', 'display_books')
    search_fields = ('subject_name', 'subject_code')
    list_filter = ('subject_name',)

    def display_books(self, obj):
        books = obj.books_subject1.all()  # Use the correct related name
        book_titles = ', '.join([book.title for book in books])
        return book_titles
    
    display_books.short_description = 'Books by this subject'

admin.site.register(Subject, SubjectAdmin)

