from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    return HttpResponse('Check')
