from .models import Page

def pages_processor(request):
    pages = Page.objects.all
    return {"pages": pages}