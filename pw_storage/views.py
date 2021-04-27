from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'pw_storage/base.html')

def about_page(request):
    return HttpResponse('<h1>Blog About</h1>')