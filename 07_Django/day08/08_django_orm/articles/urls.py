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
    # 데이터 삭제에 대한 URL 패턴
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 데이터 수정 페이지에 대한 url
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 데이터 수정 로직에 대한 url
    path('<int:pk>/update/', views.update, name='update'),
]
