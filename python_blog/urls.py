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
]