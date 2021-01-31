from django.db import models

# Create your PAGE models here.
class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    LANGUAGES = (
        ('EN', 'English'),
        ('ZH', 'Chinese'),
    )
    language = models.CharField(max_length=2, choices=LANGUAGES)
    def __str__(self):
        return self.title
