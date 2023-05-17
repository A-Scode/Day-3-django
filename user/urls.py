from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path("hello/" , Hello),
    path("hello-django/" , django_hello)
]
