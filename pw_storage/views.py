from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import urllib, hashlib
from .models import User, User_pw
from .forms import UserForm, LoginForm


def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.GET)
        if user_form.is_valid():
            if User.objects.filter(username=user_form.cleaned_data['username']).count() or User.objects.filter(email=user_form.cleaned_data['email']).count():
                return render(request, 'pw_storage/home.html')
            else:
                user_form.save()
                return render(request, 'pw_storage/user_storage.html')
    context = {'form': user_form}
    return render(request, 'pw_storage/register.html', context)


def login_page(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST, request.GET)
        if login_form.is_valid():
            if User.objects.filter(username=login_form.cleaned_data['username']).count():

                if User.objects.filter(password=login_form.cleaned_data['password']).count():
                    return render(request, 'pw_storage/user_storage.html')
                else:
                    return render(request, 'pw_storage/login.html')
    context = {'form': login_form}
    return render(request, 'pw_storage/login.html', context)

def logged_out_page(request):
    return render(request, 'pw_storage/logged_out.html')
