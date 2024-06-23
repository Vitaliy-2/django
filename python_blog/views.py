from django.shortcuts import render
from django.http import HttpResponse

CATEGORIES = {
    1: "Вы на территории Python",
    2: "Вы на территории Django",
    3: "Flask, бегите, глупцы!",
}


def category_detail(request, category_id) -> HttpResponse:
    """
    Представление для детальной страницы категории.
    blog/category/1/
    """
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    return HttpResponse(f"<h1>{category_str}</h1><a href='/category/'>Назад</a>")


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
