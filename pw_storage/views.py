from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages

# Create your views here.
from .forms import LoginForm, RegisterForm

User = get_user_model()

def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "pw_storage/register.html", {"form": form})


def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True
            messages.warning(request, 'Please enter the right password!')
    return render(request, "pw_storage/login.html", {"form": form})
  

def logged_out_page(request):
    logout(request)
    # request.user == Anon User
    return redirect("pw_storage/logged_out")