# python_blog/urls.py:
# from django.contrib import admin
from django.urls import path
from .views import blog, post_detail, category_detail, tag_detail

# Подключено через include в конфигурационном пакете
# все маршруты начинаются на blog/

urlpatterns = [
    # Добавим главную страницу
    # Добавляем категории
    # path("category/", views.category, name='categoris'),  # blog/category/
    # Добавляем детальное представление категории с int конвертером
    # path("category/<int:category_id>/", views.category_detail, name='category'),  # blog/category/1/
    # Маршрут для блога
    path("", blog, name="blog"),  # blog/
    # Маршрут с конвертером slug для отображения отдельной статьи
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('tag/<slug:slug>/', tag_detail, name='tag_detail'),
]
