from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('rand', views.random_int),
]
