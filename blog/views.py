from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Hello</2>')

def contacts(request):
    return HttpResponse('<h2>Контакты</2>')