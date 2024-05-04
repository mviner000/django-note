from django.db import models

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'subject_subject'