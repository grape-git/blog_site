from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    title = models.CharField(max_length=50, null=False)
    sub_content = models.CharField(max_length=100, null=True)
    content = models.TextField(null=False)
    content_image = models.ImageField(upload_to='content_image/', blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title