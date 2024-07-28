from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode


class Post(models.Model):
    """
    Модель поста
    """
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # related_name - имя обратной связи. Это имя будет использоваться для обращения к связанным объектам
    # Например, если мы захотим получить все посты, связанные с тегом, мы можем использовать выражение tag.posts.all()
    tags = models.ManyToManyField("Tag", related_name="posts")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        Переопределение метода save для автоматической генерации slug
        """
        if not self.slug or self.slug == '':
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)


    def __str__(self):
        """
        Строковое представление модели
        """
        return f'{self.title}: {self.slug}'


    def get_absolute_url(self):
        """
        Метод для получения абсолютного URL поста
        """
        return f'/blog/{self.slug}/'


class Category(models.Model):
    """
    Модель категории
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs) -> None:
        """
        Переопределение метода save для автоматической генерации slug
        """
        if not self.slug or self.slug == "":
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Строковое представление модели
        """
        return self.name

    # def get_absolute_url(self) -> str:
    #     """
    #     Заглушка для метода get_absolute_url
    #     """
    #     return f'/blog/category/{self.slug}/'


class Tag(models.Model):
    """
    Модель тега
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs) -> None:
        """
        Переопределение метода save для автоматического создания slug
        и приведения имени тега к нижнему регистру
        """
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        self.name = self.name.lower().replace(" ", "_")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Строковое представление модели
        """
        return self.name

    # def get_absolute_url(self) -> str:
    #     """
    #     Заглушка для метода get_absolute_url
    #     """

    #     return f'/tag/{self.slug}/'


class Comment(models.Model):
    """
    Модель комментария
    """

    STATUS_CHOICES = [
        ("checked", "Проверен"),
        ("unchecked", "Не проверен"),
    ]

    # get_user_model() - функция, которая возвращает модель пользователя, используемую в проекте
    # on_delete=models.CASCADE - при удалении пользователя, удалять все его комментарии
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    # choices - список кортежей, в котором каждый кортеж содержит два элемента: значение и человекочитаемое имя
    # Мы сможем внести в это поле только одно из значений, указанных в STATUS_CHOICES
    # default='unchecked' - значение по умолчанию
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="unchecked"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)