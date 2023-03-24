from django.contrib import admin
# 명시적 상대경로 .
# from . import models
from .models import Article
# Register your models here.

# 우리가 만든 Article 클래스를 등록
# 암기 꿀팁: admin site 에 등록(register) 하겠다
admin.site.register(Article)
