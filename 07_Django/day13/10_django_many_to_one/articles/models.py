from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 외래 키 필드(db에 article_id로 생성됨, 자동으로 _id추가됨) - 소문자 권장
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 참조하던 상대방 대상이 없어지면? on_delete=models.CASCADE 폭포처럼 떨어져서 같이 지워짐
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)