from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField
from pytils.translit import slugify

class PeopleIt(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(blank="True", max_length=255, unique=True, db_index=True, verbose_name='URL')
    who_is = models.TextField(verbose_name='Кто он')
    what_did = models.TextField(verbose_name='Что сделал')
    achievements = models.TextField(verbose_name='Достижения')
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name='Фотография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последние изменение')
    is_published =  models.BooleanField(default=True, verbose_name='Опубликовать')
    cat = ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гении IT"
        verbose_name_plural = "Гении IT"


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
