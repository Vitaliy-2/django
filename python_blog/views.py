from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}


def category_detail(request, category_id) -> HttpResponse:
    """
    Представление для детальной страницы категории.
    blog/category/1/
    """
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return HttpResponse(f"<h1>{category_str}</h1>")


def blog_catalog(request) -> HttpResponse:
    """
    Представление для главной страницы.
    """
    return HttpResponse(
        """<h1>Тут будет блог.</h1>
        """
    )


def category_list(request) -> HttpResponse:
    """
    Представление для категорий
    """
    categories = ", ".join([str(key) for key in CATEGORIES.keys()])
    return HttpResponse(categories)
