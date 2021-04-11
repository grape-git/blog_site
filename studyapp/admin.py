from django.contrib import admin

# Register your models here.
from studyapp.models import Category, Post
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Category)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'




admin.site.register(Post, PostAdmin)
