from django.contrib import admin
from commentapp.models import Comment, CommentPJ




class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'writer', 'comment_text']
    fieldsets = [
        ('작성자', {'fields':['writer']}),
        ('내용', {'fields': ['comment_text']}),
    ]

class CommentPJAdmin(admin.ModelAdmin):
    list_display = ['post', 'writer', 'comment_text']
    fieldsets = [
        ('작성자', {'fields':['writer']}),
        ('내용', {'fields': ['comment_text']}),
    ]



admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentPJ, CommentPJAdmin)