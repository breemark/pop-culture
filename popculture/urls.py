from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Pop Culture"
admin.site.site_title = "Pop Culture Shenzhen"
admin.site.index_title = "Welcome to Pop Culture System"