from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from unidecode import unidecode


# Create your PAGE models here.
class Page(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextField(blank=True, null=True)
    LANGUAGES = (
        ('en', 'English'),
        ('zh', 'Chinese'),
    )
    language = models.CharField(max_length=2, choices=LANGUAGES)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title)