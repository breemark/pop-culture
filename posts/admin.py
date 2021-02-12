from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'date_added', 'active',)

admin.site.register(Post, PostAdmin)