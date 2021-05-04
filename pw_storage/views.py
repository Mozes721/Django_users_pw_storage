from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import urllib, hashlib
from .models import User, User_pw
from .forms import UserForm

def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    user_form = UserForm
    context = {'form': user_form}
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     password1 = request.POST.get('password1')
    #     password2 = request.POST.get('password2')
    #     options = request.POST.getlist('inlineOptions')
        

    #     print(username)
    #     print(options)
    # template_name = 'register.html'
    # fields = '__all__'
    return render(request, 'pw_storage/register.html', context)

def login_page(request):
    return render(request, 'pw_storage/login.html')

def logged_out_page(request):
    return render(request, 'pw_storage/logged_out.html')
