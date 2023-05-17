from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Hello(request):
    return HttpResponse("<h1 align='center' >Hello</h1>")


def django_hello(request):
    
    return render(request , "hello.html" ,{})

