from django.shortcuts import render
from django.http import HttpResponse
from .models import Page


def index(request):
    pages = Page.objects.all
    return render(request, 'home.html', {'pages': pages})