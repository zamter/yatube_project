# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name = 'posts'),

    #Страница групп
    path('group/<slug:slug>/', views.group_posts, name = 'group_list')    
]