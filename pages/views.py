from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from posts.models import Post


def index(request):
    main_page = Page.objects.get(slug='main')
    posts = Post.objects.all
    return render(request, 'home.html', {'posts': posts, 'main_page': main_page})

def page_content(request, slug):
    page = Page.objects.get(slug=slug)
    if page != 'admin' or page != 'posts':
        return render(request, 'page.html', {'page': page})
