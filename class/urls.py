from django.urls import path
from .views import home

app_name = 'class'

urlpatterns = [
    path('', home),
]
