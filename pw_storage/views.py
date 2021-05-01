from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import pymongo
import urllib, hashlib
from .models import User

client = pymongo.MongoClient("mongodb://localhost:27017/?")
# Create your views here.

#databases
users = client.get_database('users_stored')
user_pw_storage = client.get_database('pw_storage_user')

def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    user = User.objects
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        options = request.POST.getlist('inlineOptions')
        
        print(username)
        print(options)
    return render(request, 'pw_storage/register.html')

def login_page(request):
    return render(request, 'pw_storage/login.html')

def logged_out_page(request):
    return render(request, 'pw_storage/logged_out.html')
