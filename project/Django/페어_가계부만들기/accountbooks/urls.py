from django.urls import path
from . import views
app_name = 'accountbooks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:account_book_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:account_book_pk>/edit/', views.edit, name='edit'),
    path('<int:account_book_pk>/update/', views.update, name='update'),
    path('<int:account_book_pk>/delete/', views.delete, name='delete'),
    path('<int:account_book_pk>/copy/', views.copy, name='copy'),
    path('select/', views.select, name='select'),
    # path('<str:account_category>/order1/', views.order1, name='order1'),
    # path('<str:account_category>/order2/', views.order2, name='order2'),
    # path('<str:account_category>/order3/', views.order3, name='order3'),
]
