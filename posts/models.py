from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from unidecode import unidecode


# Create your POST models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextField(blank=True, null=True)
    LANGUAGES = (
        ('EN', 'English'),
        ('ZH', 'Chinese'),
    )
    language = models.CharField(max_length=2, choices=LANGUAGES)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField('date published', auto_now_add=True)


    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title)