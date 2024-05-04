# Generated by Django 5.0.4 on 2024-05-02 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('controlno', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('edition', models.CharField(blank=True, max_length=255, null=True)),
                ('pagination', models.CharField(blank=True, max_length=255, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('pubplace', models.CharField(blank=True, max_length=255, null=True)),
                ('copyright', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, max_length=255, null=True)),
                ('series_title', models.CharField(blank=True, max_length=255, null=True)),
                ('aentrytitle', models.CharField(blank=True, max_length=255, null=True)),
                ('allno', models.CharField(blank=True, max_length=255, null=True)),
                ('aeauthor1_code', models.ForeignKey(blank=True, db_column='aeauthor1_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aeauthor1_books', to='author.author')),
                ('aeauthor2_code', models.ForeignKey(blank=True, db_column='aeauthor2_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aeauthor2_books', to='author.author')),
                ('aeauthor3_code', models.ForeignKey(blank=True, db_column='aeauthor3_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aeauthor3_books', to='author.author')),
                ('author_code', models.ForeignKey(db_column='author_code', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='author.author')),
                ('subject1_code', models.ForeignKey(blank=True, db_column='subject1_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_subject1', to='subject.subject')),
                ('subject2_code', models.ForeignKey(blank=True, db_column='subject2_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_subject2', to='subject.subject')),
                ('subject3_code', models.ForeignKey(blank=True, db_column='subject3_code', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_subject3', to='subject.subject')),
            ],
            options={
                'db_table': 'book_book',
            },
        ),
    ]
