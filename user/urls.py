from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path("hello/" , Hello),
    path("hello-django/" , django_hello),
    path("student/"  , include("user.student.urls") ),
    path("staff/"  , include("user.staff.urls") )
]
