# from email import message
# from re import search
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404


# page_alias - переменная, которая содержит алиас текущей страницы.
# Чтобы сделать её "активной"
# Нужно передать это значение через контекст в шаблон!!!

menu = [
    {
        "name": "Главная",
        "alias": "main"
    },
    {
        "name": "Блог",
        "alias": "blog"
    },
    {
        "name": "О проекте",
        "alias": "about"
    }
]


def index(request) -> HttpResponse:
    """
    Функция - представление для главной страницы
    Принимает объект запроса HttpRequest
    Вносит контекст дополнительные данные.
    """
    context = {
        "menu": menu,
        "page_alias": "main",
        "title": "Главная страница"
    }
    return render(request, 'index.html', context)


def about(request):
    """
    Вьюшка для страницы "О проекте"
    """
    context = {
        "menu": menu,
        "page_alias": "about",
        "title": "О нас"
    }
    return render(request, 'python_blog/about.html', context)


def blog(request):
    """
    Вьюшка для страницы "Блог" с каталогом постов.
    Обрабатываем поисковую форму, которая обрабатывается методом GET
    И пробуем получить от туда ключи:
        search
        searchInTitle
        searchInText
        searchInTags
    """
    
    if request.method == "GET":  # Проверка на гет-запрос
        posts = Post.objects.all()
      
        context = {
            "menu": menu,
            "page_alias": "blog",
            "posts": posts,
        }
        return render(request, 'python_blog/blog.html', context)


def post_detail(request, slug):
    """
    Функция - представление для отдельной статьи
    Принимает объект запроса HttpRequest и slug статьи
    Отображает статью с соответствующим slug
    """
    # Это первый вариант добычи
    # post = Post.objects.get(slug=slug)
    # Есть второй вариант добычи поста по slug
    # post = Post.objects.filter(slug=slug).first()

    # И самый надежный
    # get_object_or_404- метод, который возвращает объект или 404

    post = get_object_or_404(Post, slug=slug)


    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog_catalog",
    }
    return render(request, "python_blog/post_detail.html", context)


# def tag_detail(request, slug: str):
#     """
#     Функция - представление для страницы тега
#     Принимает объект запроса HttpRequest и slug тега
#     Отображает список статей с соответствующим slug

#     Как это было бы на SQL (многие ко многим)

#     SELECT * FROM post WHERE id IN (
#         SELECT post_id FROM post_tags WHERE tag_id = (
#             SELECT id FROM tag WHERE slug = slug
#         )
#     )
#     """
#     posts = Post.objects.filter(tags__slug=slug)
#     context = {
#         "menu": menu,
#         "posts": posts,
#         "page_alias": "blog_catalog",
#     }

#     return render(request, "blog/blog_catalog.html", context)



