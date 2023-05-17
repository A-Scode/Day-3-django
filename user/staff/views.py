from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request , "dashboard.html" , {"user_type" : "Staff" , "user_name" : "SomeName"})
