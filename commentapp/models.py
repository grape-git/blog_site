from django.db import models

# Create your models here.
from projectapp.models import Project
from studyapp.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    writer = models.CharField(max_length=20 ,null=False)
    email = models.EmailField(max_length=50, blank=True, null=True)
    comment_text = models.TextField(null=False)
    create_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment_text

class CommentPJ(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='commentpj')
    writer = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, blank=True, null=True)
    comment_text = models.TextField(null=False)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text


    def __str__(self):
        return self.comment_text