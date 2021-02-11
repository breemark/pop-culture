from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>', views.page_content, name='page_content')
]