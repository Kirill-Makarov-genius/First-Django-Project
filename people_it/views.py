from django.urls.base import reverse_lazy
from people_it.utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView
from people_it.forms import *
from .models import *

class Home(DataMixin, ListView):
    model = PeopleIt
    template_name = 'people_it/main.html'
    context_object_name = 'people'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_user_context(title="Главная страница")

        return dict(list(context.items()) + list(add_context.items()))

class Categories(LoginRequiredMixin, DataMixin, ListView):
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

class AddPost(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'people_it/add_post.html'
    context_object_name = 'form'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = self.get_user_context(title="Создание поста", cat_selected=None)
        
        return dict(list(context.items()) + list(add_context.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "people_it/register.html"
    success_url = reverse_lazy("login")


def work(request):
    return HttpResponse('Work')




def PageNotFound(request, exception):
    return HttpResponseNotFound("Ошибка")
