from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 정참조인데 자기자신 일때 역참조 이름 만들어줘야 함
    # symmetrical 기본값 True 대칭이라서 바꿔줘야 함
