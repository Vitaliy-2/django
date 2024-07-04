from email import message
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
    context: dict[str, str | None] = {"message": category_str}
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return render(request, "python_blog/test_template.html", context=context)


def index(request) -> HttpResponse:
    """
    Представление для главной страницы.
    """
    return HttpResponse(
        """<h1>Тут будет блог.</h1>
        """
    )


def category(request) -> HttpResponse:
    """
    Представление для категорий
    """
    categories = ", ".join([str(key) for key in CATEGORIES.keys()])
    return HttpResponse(categories)


class Developer:
    def __init__(self, name, stack: list):
        self.name = name
        self.stack = stack

    def __str__(self):
        return f"{self.name} - {self.stack}"

    def get_rus_info(self):
        return f"Разработчик {self.name} - {', '.join(self.stack)}"


about_data = {
    "title": "О нас",
    "text": "Мы - команда разработчиков",
    "stack_list": ["Python", "Dgango", "Flask"],
    "developers": [
        {"name": "Иван",
        "age": 25,
        "stack": ["Python", "Django"],
        "is_active": True},
        {"name": "Анна",
        "age": 23,
        "stack": ["Python", "Flask"],
        "is_active": True},
        {"name": "Петр",
        "age": 30,
        "stack": ["JS", "React", "Vue"],
        "is_active": False},
    ]
}


# Представление которое отрисует about.html
def about(request) -> HttpResponse:
    return render(request, "python_blog/about.html", about_data)
