from django.shortcuts import render

# ice_cream/views.py
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница конкретной группы
def group_posts(request, slug):
    return HttpResponse(f'Страница группы {slug}')