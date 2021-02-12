from .models import Page

def pages_processor(request):
    pages = Page.objects.exclude(slug='main')
    return {"pages": pages}