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
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.GET)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if User.objects.filter(username=form.cleaned_data['username']).count() or User.objects.filter(email=form.cleaned_data['email']).count():
                return render(request, 'pw_storage/home.html')
            else:
                form.save()
                return render(request, 'pw_storage/user_storage.html')
    context = {'form': form}
    return render(request, 'pw_storage/register.html', context)


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST, request.GET)
        if form.is_valid():
            return render(request, 'pw_storage/user_storage.html')
        else:
            messages.error(request, "Please enter correct username and password")
    return render(request = request,
                     template_name = "pw_storage/login.html",
                     context={ "login_form": form })

    #     if form.is_valid():
    #         if User.objects.filter(username=form.cleaned_data['username']).count():
    #             print(User.objects.filter(username=form.cleaned_data['username']).count())
    #             if User.objects.filter(password=form.cleaned_data['password']).count():
    #                 print(User.objects.filter(password=form.cleaned_data['password']).count())
    #                 return render(request, 'pw_storage/user_storage.html')
    #             else:
    #                 context = {'login_form': form}
    #                 return render(request, 'pw_storage/login.html', context)
    #         return render(request, 'pw_storage/login.html')
    # context = {'login_form': form}
    # return render(request, 'pw_storage/login.html', context)

# def login_page(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST, request.GET)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print(username)
#             print(password)
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request = request,
#                     template_name = "pw_storage/login.html",
#                     context={"form":form})


def logged_out_page(request):
    return render(request, 'pw_storage/logged_out.html')
