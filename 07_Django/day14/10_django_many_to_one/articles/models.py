from django.db import models
# from accounts.models import User 비추천: 직접 참조할 수 있지만. 장고에서 간접 참조 함수 제공 하고 권장
# ​get_user_model "현재 프로젝트에 활성화"된 "User 객체"를 반환해주는 함수
# 다른 이름으로 상속 받아서 custom 해서 재정의 부분만 덮어씌움 accounts forms 참고
# user model은 추가적으로 생각해야할 것 있음

# 이전에 배웠던 get_user_model 함수 사용(models.py에서는 사용하지 않음)
# from django.contrib.auth import get_user_model

# settings.py 에 AUTH_USER_MODEL = 'accounts.User' => settings.AUTH_USER_MODEL 이거 가져다 쓰는건데.. 이거는 문자열이다 객체 아니다

# Django 내부 실행 원리(순서).. 나중에 user가 만들어졌을 때 문자열로 참조하게 함.그래야 정상 순서. user객체 사용하면 에러가 발생함.

# 유저 모델 참조 방법 2가지 get_user_model() 과 settings.AUTH_USER_MODEL 2가지
# 반환 되는 타입이 다름. 
# get_user_model() vs settings.AUTH_USER_MODEL /객체 vs 문자열/ models.py가 아닌 모든 곳에서 참조할 때 사용 vs models.py 모델 필드에서 참조할 때 사용

# models.py에서 User를 참조할땨만 다음과 같이 참조한다.
from django.conf import settings

# 마이그레이션 하면.. user default 기본값 설정하라고 나옴

# Create your models here.
class Article(models.Model):
    # user 소문자 + 단수형
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # # Article 클래스의 출력을 객체가 아니라 타이틀로 바꿔줌
    # def __str__(self):
    #     return self.title

class Comment(models.Model):
    # 외래 키 필드
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)