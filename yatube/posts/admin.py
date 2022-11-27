from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    #Поля для отображения в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    # Изменение поля group прямо из списка постов
    list_editable = ('group',)
    # Интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Возможность фильтрации по дате
    list_filter = ('pub_date',)
    # Свойство для отображения в пустых колонках
    empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Group)