from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    temp_id = models.IntegerField(blank=True, null=True)
    author_code = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'author_author'