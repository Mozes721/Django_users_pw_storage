from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
from .forms import *
from .models import User_pw

User = get_user_model()

 
def home_page(request):
    return render(request, 'pw_storage/home.html')

def register_page(request):
    form = RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in as  %s " % request.user + " you can't register or login ones already logged in!")
        return redirect(home_page)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
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
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in as %s" % request.user + " you can't register or login ones already logged in!")
        return redirect(home_page)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(user_pw_all)
        else:
            messages.warning(request, 'Please enter the right password!')
    return render(request, "pw_storage/user_account/login.html", {"form": form})
  
@login_required(login_url=login_page)
def logged_out_page(request):
    logout(request)
    return render(request, "pw_storage/user_account/logged_out.html")
    
@login_required(login_url=login_page)
def user_pw_all(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    logged_in_user = request.user  
    logged_in_user_pws = User_pw.objects.filter(user=logged_in_user).order_by('-date')
    if not logged_in_user_pws:
        message = 'Please create a password'
        return render(request, "pw_storage/user_password/user_pw_all.html", {'no_pws': message})
    
    return render(request, "pw_storage/user_password/user_pw_all.html", {'pws': logged_in_user_pws})

@login_required(login_url=login_page)
def user_pw_add(request):
    form = User_pw_form(request.POST or None)
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    logged_in_user = request.user
    if form.is_valid():
        title = form.cleaned_data.get("title")
        password = form.cleaned_data.get("password")
        type = form.cleaned_data.get("type")
        try:
            User_pw.objects.create(title=title, password=password, type=type, user=logged_in_user)
            messages.success(request, "---Sucesfully added new pw field for your storage---")
        except Exception as e:
            raise e
            
    return render(request, "pw_storage/user_password/user_pw_add.html", {'form': form})
 
@login_required(login_url=login_page)
def user_pw_search(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    logged_in_user = request.user  
    logged_in_user_pws = User_pw.objects.filter(user=logged_in_user)
    if request.method == "POST":
        searched = request.POST.get("password_search", "")
        # user_pw = logged_in_user_pws.filter(name__contains=searched)
        users_pws = logged_in_user_pws.values()
        if users_pws.filter(title=searched):
            user_pw = User_pw.objects.filter(Q(title=searched)).values()
            return render(request, "pw_storage/user_password/user_pw_search.html", {'user_pw': user_pw})
        else:
            messages.error(request, "---YOUR SEARCH RESULT DOESN'T EXIST---")
            print("NOT FOUND")

    return render(request, "pw_storage/user_password/user_pw_search.html", {'pws': logged_in_user_pws})


@login_required
def edit(request, task_id):
    if request.method == "POST":
        if request.POST['title'] and request.POST['description']:
            task = Task(pk=task_id)
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.pub_date = timezone.datetime.now()
            task.completed = False
            task.user = request.user
            task.save(pk=task_id)
            return render(request, 'home/taskdetail.html', {'task':task})
        else:
           return render(request, 'home/create.html', {'error':'All fields are required'})
    else:
        return render(request, 'home/create.html')
