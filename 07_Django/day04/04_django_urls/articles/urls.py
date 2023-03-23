from django.urls import path
# 명시적 상대경로 (. 현재위치 django 권장사항)
from . import views


app_name = 'articles'
# 각각의 이름 앞에 명찰이 붙음 articles:dinner
# 붙인 이후에는 단독으로 사용 안되고 명찰이름 무조건 붙여야 됨
# NoReverseMatch 에러 나오면 무조건 URL관련문제

urlpatterns = [
    path('index/', views.index, name='index'),
    # name='index' 로 이름 정하기
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('<int:num>/', views.detail, name='detail'),
    path('hello/<str:name>/', views.hello, name='hello')
]
