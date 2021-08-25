from people_it.utils import DataMixin
from django.db import models
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView
from .models import *

class Home(DataMixin, ListView):
    model = PeopleIt
    template_name = 'people_it/main.html'
    context_object_name = 'people'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_user_context(title="Главная страница")

        return dict(list(context.items()) + list(add_context.items()))

class Categories(DataMixin, ListView):
    model = PeopleIt
    template_name = 'people_it/main.html'
    context_object_name = 'people'
    def get_queryset(self):
        return PeopleIt.objects.filter(cat__slug = self.kwargs["cat_slug"])

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        add_context = self.get_user_context(title = context["people"][0].cat.name, cat_selected = context["people"][0].cat)

        return dict(list(context.items()) + list(add_context.items()))



class ShowPost(DataMixin, DetailView):
    model = PeopleIt
    template_name = 'people_it/post.html'
    context_object_name = 'person'
    slug_url_kwarg = 'post_slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_user_context(title=context["person"].name, cat_selected=None)
        
        return dict(list(context.items()) + list(add_context.items()))



def about(request):
    return HttpResponse('About')

def add_post(request):
    return HttpResponse('Add post')

def work(request):
    return HttpResponse('Work')

def login(request):
    return HttpResponse('Login')


def PageNotFound(request, exception):
    return HttpResponseNotFound("Ошибка")
