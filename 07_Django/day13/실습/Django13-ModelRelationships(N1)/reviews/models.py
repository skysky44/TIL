from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='reviews')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    movie = models.CharField(max_length=20)
