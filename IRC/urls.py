from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.channels, name='channels'),
    path('<int:id>/', views.channel, name='channel')
]
