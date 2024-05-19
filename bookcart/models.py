from django.db import models
from django.utils import timezone
from book.models import Book

class BookCart(models.Model):
    student = models.CharField(max_length=200, blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='book_carts')
    is_borrowed_verified = models.BooleanField(default=False)
    set_to_return = models.BooleanField(default=False)
    borrowed_verified_by = models.CharField(max_length=255, blank=True, null=True)
    is_returned_verified = models.BooleanField(default=False)
    returned_verified_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book_cart'
