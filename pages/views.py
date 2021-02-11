from django.shortcuts import render
from django.http import HttpResponse
from .models import Page


def index(request):
    pages = Page.objects.all
    return render(request, 'home.html', {'pages': pages})

def page_content(request, slug):
    page = Page.objects.get(slug=slug)
    if page != 'admin':
        return render(request, 'page.html', {'page': page})
