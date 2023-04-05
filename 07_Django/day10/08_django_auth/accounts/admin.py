from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User
# 공식 문서에 있어서 외울필요는 없음


admin.site.register(User, UserAdmin)
