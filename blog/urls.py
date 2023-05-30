from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]