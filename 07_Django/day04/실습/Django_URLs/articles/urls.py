from django.urls import path
# 명시적 상대경로 (. 현재위치 django 권장사항)
from . import views

app_name = 'articles'

urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path("number-print/", views.number_print_index, name="number-print-index"),
    path('number-print/<int:number>/', views.number_print, name='number-print'),
    path('calculate/',
         views.calculate_index, name='calculate-index'),
    path('calculate/<int:number1>/<int:number2>/',
         views.calculate, name='calculate'),
]
