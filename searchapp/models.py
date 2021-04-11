from django.db import models

# Create your models here.


class Search(models.Model):
    text = models.CharField(max_length=50, null=False)
