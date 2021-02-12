from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def post_content(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'page.html', {'post': post})
