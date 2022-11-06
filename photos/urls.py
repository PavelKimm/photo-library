from django.urls import path
from photos.views import home

urlpatterns = [
    path('', home, name='home-page'),
]
