from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField, TextField

class PeopleIt(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    who_is = models.TextField()
    what_did = models.TextField()
    achievements = models.TextField()
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published =  models.BooleanField(default=True)
    cat = ForeignKey('Category', on_delete=models.PROTECT)

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
