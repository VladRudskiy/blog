from django.db import models
from django.urls import reverse


class artist(models.Model):
    title = models.CharField(max_length=255,verbose_name='Заголовок статьи')
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name='URL')
    content = models.TextField(blank=True,verbose_name='Содержимое статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True,verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"
        ordering = ['time_create','title']