from django.db import models

# Create your models here.
class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='임의 경로')