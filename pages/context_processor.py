from .models import Page

def pages_processor(request):
    language_string = request.path.strip("/")
    split_language_string = language_string.split("/", 1)
    language = split_language_string[0]

    if language == 'en':
        language_opposite = 'zh'
    else:
        language_opposite = 'en'


    pages = Page.objects.all().filter(language=language, active=True,).exclude(slug='main').exclude(slug='main-chinese')

    return {"pages": pages, 'language':language, 'language_opposite': language_opposite}