from django.db import models

# Create your models here.
class noval(models.Model):
    title = models.CharField(max_lenght=255)
    body = models.TextField()