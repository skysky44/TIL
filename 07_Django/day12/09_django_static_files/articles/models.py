from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # MEDIA_ROOT 이후의 추가 경로를 설정 => upload_to='images/'
    # 날짜폴더로 넣고 싶을때 upload_to='%Y/%m/%d'
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
