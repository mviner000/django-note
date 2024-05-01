from django.db import models
from author.models import Author

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    controlno = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author_code = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', db_column='author_code')
    edition = models.CharField(max_length=255, blank=True, null=True)
    pagination = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    pubplace = models.CharField(max_length=255, blank=True, null=True)
    copyright = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    subject1_code = models.CharField(max_length=255, blank=True, null=True)
    subject2_code = models.CharField(max_length=255, blank=True, null=True)
    subject3_code = models.CharField(max_length=255, blank=True, null=True)
    series_title = models.CharField(max_length=255, blank=True, null=True)
    aentrytitle = models.CharField(max_length=255, blank=True, null=True)
    aeauthor1_code = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='aeauthor1_books', db_column='aeauthor1_code')
    aeauthor2_code = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='aeauthor2_books', db_column='aeauthor2_code')
    aeauthor3_code = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='aeauthor3_books', db_column='aeauthor3_code')
    allno = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'book_book'