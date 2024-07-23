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
    tags = models.JSONField(null=True, blank=True, default=list)
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
