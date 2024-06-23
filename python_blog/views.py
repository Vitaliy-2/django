from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    """
    Представление для главной страницы.
    """
    return HttpResponse(
        """<h1>Мой блог!</h1>
        <a href="/category/">Категории</a>
        """
    )  # вернет страницу с заголовком с этой надписью


def category(request) -> HttpResponse:
    """
    Представление для категорий
    """
    return HttpResponse(
        """<ul><li>Python</li><li>Django</li><li>Flask</li></ul>
        <a href="/">На главную</a>
        """
    )  # Вернет страницу со списком
