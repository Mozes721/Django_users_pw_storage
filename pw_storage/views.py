from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            return redirect(user_pw_all)
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "pw_storage/user_account/register.html", {"form": form})


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
            return redirect(user_pw_all)
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True
            messages.warning(request, 'Please enter the right password!')
    return render(request, "pw_storage/user_account/login.html", {"form": form})
  
@login_required(login_url=login_page)
def logged_out_page(request):
    logout(request)
    return render(request, "pw_storage/user_account/logged_out.html")
    g
@login_required(login_url=login_page)
def user_pw_all(request):
    return render(request, "pw_storage/user_password/user_pw_all.html")

@login_required(login_url=login_page)
def user_pw_add(request):
    return render(request, "pw_storage/user_password/user_pw_add.html")

@login_required(login_url=login_page)
def user_pw_search(request):
    return render(request, "pw_storage/user_password/user_pw_search.html")


