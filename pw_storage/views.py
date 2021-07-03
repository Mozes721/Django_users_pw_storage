from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.template import RequestContext
import urllib, hashlib
from .models import User, User_pw
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
import pdb
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        password1 = form.cleaned_data.get('password1')
        gender = form.cleaned_data.get('gender')
        try:
            user = User.objects.create_user(request, username=username, firstname=firstname, lastname=lastname, email=email, password=password, gender=gender)
        except:
            user = None 
        if user != None:
            return redirect("home")
        else:
            request.session['register_error'] = 1
        return render(request, '.pw_storage/user_storage.html')
    return render(request, 'pw_storage/register.html', {'form': form})


def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("user_storage")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True
    return render(request, "login.html", {"form": form})


def logged_out_page(request):
    return render(request, 'pw_storage/logged_out.html')
