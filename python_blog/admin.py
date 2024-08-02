from calendar import c
from django.contrib import admin
from .models import Post, Category, Tag, Comment


# admin.site.register(Post)

# Вариант с классом
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в админке
    list_display = ("title", "author", "published_date", "updated_date")
    # Поля, по которым можно будет искать
    search_fields = ("title", "text")
    # Поля, по которым можно будет фильтровать
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
