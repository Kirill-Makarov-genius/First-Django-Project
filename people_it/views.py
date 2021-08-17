from django.db import models
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView
from .models import *

class Home(ListView):
    model = PeopleIt
    template_name = 'people_it/base.html'
    context_object_name = 'people'

def PageNotFound(request, exception):
    return HttpResponseNotFound("Ошибка")
