from django.shortcuts import render
from django.http import HttpResponse

def index(request) -> HttpResponse:
    return HttpResponse("Привет, Python315!") # вернет страницу с этой надписью
