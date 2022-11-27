from django.shortcuts import render, get_object_or_404
# Импорт моделей для обращения к ним
from .models import Post, Group

# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    template = 'posts/index.html'
    context = {
        'posts': posts,
        'title' : title
    }
    return render(request, template, context)

# Страница конкретной группы
def group_posts(request, slug):
    # Функция для возврата сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)