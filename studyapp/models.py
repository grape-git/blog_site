from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    study_title = models.CharField(max_length=50, null=False)
    study_image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.study_title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    post_title = models.CharField(max_length=50, null=False)
    sub_content = models.CharField(max_length=100, null=True)
    post_content = models.TextField(null=False)
    content_image = models.ImageField(upload_to='content_image/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.post_title
