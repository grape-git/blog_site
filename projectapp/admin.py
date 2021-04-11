from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from projectapp.models import Project


class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Project, ProjectAdmin)