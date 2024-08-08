from django.contrib import admin
from django.urls import path, include
from python_blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='main'),
    # Добавим пакетно pythom_blog.urls
    path("blog/", include("python_blog.urls")),
    # Добавляем страницу about
    path("about/", views.about, name="about"),
]

# Необходимо для динамических изменений картинок и других файлов
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),

