from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<language>', views.main_page, name='main_page'),
    path('<language>/<slug>', views.page_content, name='page_content')
]