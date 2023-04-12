from django.contrib import admin
from .models import Article, Comment
# Register your models here.

# admin 사이트에 등록한다()
admin.site.register(Article)
admin.site.register(Comment)