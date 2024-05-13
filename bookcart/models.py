from django.db import models
from book.models import Book

class BookCart(models.Model):
    student = models.CharField(max_length=200, blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='book_carts')
    is_borrowed_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'book_cart'