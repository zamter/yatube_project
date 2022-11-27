# posts/views.py
from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title' : title
    }
    return render(request, 'posts/index.html', context)


# Страница конкретной группы
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title' : title,
        'slug' : slug
    }
    return render(request, template, context)