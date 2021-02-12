from django.urls import path
from . import views

urlpatterns = [
    path('<post>', views.post_content, name='post_content')
]