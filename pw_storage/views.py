from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    return render(request, 'pw_storage/register.html')

def login_page(request):
    return render(request, 'pw_storage/login.html')

def logged_out_page(request):
    return render(request, 'pw_storage/logged_out.html')
