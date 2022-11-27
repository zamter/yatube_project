from django.db import models
# Из модуля auth импортируем функцию get_user_model 
from django.contrib.auth import get_user_model

# Create your models here.

#Обращение к модели User через функцию get_user_model()
User = get_user_model()

#Объявление класса Post как наследника класса Model модуля models

class Group(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        #author ссылается на автора поста, на модель User, и для этого поля указано свойство related_name='posts'
        related_name='posts'
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="posts", blank=True, null=True)
