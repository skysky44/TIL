from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # ​variable routing
    # 콜론 기준 왼쪽 타입 오른쪽 변수명
    # 상세 주소 articles/1
]
