from .models import Page

def pages_processor(request):
    language_string = request.path.strip("/")
    split_language_string = language_string.split("/", 1)
    language = split_language_string[0]

    if language == 'en':
        language_opposite = 'zh'
        language_name = '中文 🇨🇳'

    else:
        language_opposite = 'en'
        language_name = 'English 🇬🇧'

    pages = Page.objects.all().filter(language=language, active=True,).exclude(slug='main').exclude(slug='main-chinese')

    return {"pages": pages, 'language':language, 'language_opposite': language_opposite, 'language_name': language_name}