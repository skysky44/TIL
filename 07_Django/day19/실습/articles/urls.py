from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comments_create),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
]
