from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.db.models import F, Q


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

        # Просто, но не оптимально
        # posts = Post.objects.all()

        # Говорим, чтобы при обращении к БД добылись сразу все теги и категории,
        # за один запрос. А в целом также будет добыт весь экземпляр класса в переменную posts.
        posts = Post.objects.prefetch_related("tags", "category").all().order_by("-published_date")
        search = request.GET.get("search")
        
        # Если что-то есть в поиске, есть смысл его обрабатывать
        if search:
            search_in_title = request.GET.get("search_in_title")
            search_in_text = request.GET.get("search_in_text")
            search_in_tags = request.GET.get("search_in_tags")

            # Формируем Q объект, который будем наполнять по мере активации чекбоксов
            query = Q()

            # Заменяю лукап icontains на iregex т.к. SQLite не приводит к регистру кирилицу.
            # Обработка чекбокса поиска в заголовке
            if search_in_title:
                query |= Q(title__iregex=search)
            # Обработка чекбокса поиска в тексте
            if search_in_text:
                query |= Q(text__iregex=search)
            # Обработка чекбокса поиска в тегах
            if search_in_tags:
                query |= Q(tags__name__iregex=search)

            # Если чекбоксы не активированы, ищем только по тексту поста
            if not search_in_title and not search_in_text and not search_in_tags:
                query = Q(text__iregex=search)

            # Сортировка по дате публикации
            posts = posts.filter(query).distinct()
      
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

    # post = get_object_or_404(Post, slug=slug)

    # prefetch_related - позволяет сделать запрос к связанным объектам
    post = Post.objects.prefetch_related("tags", "category").get(slug=slug)

    # Проверяем, есть ли в сессии информация о просмотренных постах
    if 'viewed_posts' not in request.session:
        request.session['viewed_posts'] = []
    
    # Если пост еще не был просмотрен, увеличиваем количество просмотров
    
    if slug not in request.session['viewed_posts']:
        post.views = F('views') + 1
        post.save(update_fields=['views'])
        request.session['viewed_posts'].append(slug)  # Добавляем пост в список просмотренных
        request.session.modified = True  # Указываем, что сессия была изменена для сохранения изменений
    


    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog_catalog",
    }
    return render(request, "python_blog/post_detail.html", context)


def category_detail(request, slug):
    """
    Функция - представление для страницы категории
    Принимает объект запроса HttpRequest и slug категории
    Отображает список статей с соответствующим slug

    Как это было бы на SQL

    SELECT * FROM post WHERE category_id = (
        SELECT id FROM category WHERE slug = slug
    )
    """
    posts = Post.objects.filter(category__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog_catalog",
    }

    return render(request, "python_blog/blog.html", context)


def tag_detail(request, slug):
    """
    Функция - представление для страницы тега
    Принимает объект запроса HttpRequest и slug тега
    Отображает список статей с соответствующим slug

    Как это было бы на SQL (многие ко многим)

    SELECT * FROM post WHERE id IN (
        SELECT post_id FROM post_tags WHERE tag_id = (
            SELECT id FROM tag WHERE slug = slug
        )
    )
    """
    posts = Post.objects.filter(tags__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog_catalog",
    }

    return render(request, "python_blog/blog.html", context)



