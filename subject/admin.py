from django.contrib import admin
from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code')  # Display these fields in the admin list
    search_fields = ('subject_name', 'subject_code')  # Enable search on these fields
    list_filter = ('subject_name',)  # Add filters based on these fields

admin.site.register(Subject, SubjectAdmin)
