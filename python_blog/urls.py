# python_blog/urls.py:
from django.contrib import admin
from django.urls import path
from python_blog import views

# Подключено через include в конфигурационном пакете
# все маршруты начинаются на blog/

urlpatterns = [
    # Добавим главную страницу
    path("", views.index),
    # Добавляем категории
    path("category/", views.category),  # blog/category/
    # Добавляем детальное представление категории с int конвертером
    path("category/<int:category_id>/", views.category_detail),  # blog/category/1/
]
