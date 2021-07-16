from django.contrib import admin
from .forms import *
from .models import User_pw, User


# Register your models here.
admin.site.register(User_pw)
#admin.site.register(User)