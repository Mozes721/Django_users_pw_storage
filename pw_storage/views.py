from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import RequestContext
import urllib, hashlib
from .models import User, User_pw
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
import pdb
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.GET)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).count() or User.objects.filter(email=form.cleaned_data['email']).count():
                return render(request, 'pw_storage/home.html')
            else:
                form.save()
                return render(request, 'pw_storage/user_storage.html')
    context = {'register_form': form}
    return render(request, 'pw_storage/register.html', context)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'pw_storage/user_storage.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please write your username and password or create a account")
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
