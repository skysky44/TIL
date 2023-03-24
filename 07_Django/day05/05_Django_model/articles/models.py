from django.db import models

# Create your models here.


class Article(models.Model):
    # 필드 이름(변수명) title / 데이터 타입(모델 필드 클래스) CharField / 제약조건(모델 필드 클래스의 키워드 인자) max_length=10
    # CharField() 길이제한 o, TextField() 길이제한 x
    # id 필드는 자동 생성
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 이후에 두개의 필드를 추가
