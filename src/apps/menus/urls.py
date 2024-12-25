from django.urls import path

from src.apps.menus.views import home

app_name = 'menus'
urlpatterns = [
    path("", home, name='home')
]
