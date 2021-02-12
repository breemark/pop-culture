from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Page
from posts.models import Post


def index(request):
    response = redirect('/en')
    return response

def main_page(request, language):
    if language == '':
        language = 'en'
        main_page = Page.objects.get(slug='main')
    elif language == 'zh':
        main_page = Page.objects.get(slug='main-chinese')
    else:
        main_page = Page.objects.get(slug='main')
    
    posts = Post.objects.all
    return render(request, 'home.html', {'posts': posts, 'main_page': main_page})

def page_content(request, language, slug):
    page = Page.objects.get(slug=slug)
    if page != 'admin' or page != 'posts':
        return render(request, 'page.html', {'page': page})
