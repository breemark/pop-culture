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

    # The 'main' page and the 'main-chinese' page should not be deleted, because they are the front pages of the website. 
    pages = Page.objects.all().filter(language=language, active=True,).exclude(slug='main').exclude(slug='main-chinese')

    return {"pages": pages, 'language':language, 'language_opposite': language_opposite, 'language_name': language_name}