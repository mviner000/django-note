from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from author.models import Author
from subject.models import Subject

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
    subject1_code = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='books_subject1', db_column='subject1_code')
    subject2_code = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='books_subject2', db_column='subject2_code')
    subject3_code = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True, related_name='books_subject3', db_column='subject3_code')
    series_title = models.CharField(max_length=255, blank=True, null=True)
    aentrytitle = models.CharField(max_length=255, blank=True, null=True)
    aeauthor1_code = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='aeauthor1_books', db_column='aeauthor1_code')
    aeauthor2_code = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='aeauthor2_books', db_column='aeauthor2_code')
    aeauthor3_code = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='aeauthor3_books', db_column='aeauthor3_code')
    allno = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_url = CloudinaryField('image', folder='books', blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_width = models.PositiveIntegerField(blank=True, null=True)
    thumbnail_height = models.PositiveIntegerField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    stock_quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'book_book'

# Signal receiver to copy thumbnail_url to image_url after saving
@receiver(post_save, sender=Book)
def copy_thumbnail_to_image_url(sender, instance, **kwargs):
    if kwargs.get('created') or kwargs.get('update_fields'):
        instance.image_url = instance.thumbnail_url
        instance.save(update_fields=['image_url'])