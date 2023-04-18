from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/', views.profile, name = 'profile'),
        #str: 생략가능
        # username 밑에 다른 url은 작동 안함
        # 1. 맨아래에 두기 2. 'profile/<username>/로 섞어주기 두가지 방법
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
