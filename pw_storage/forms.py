from django import forms
from django.forms import fields 
from .models import User, User_pw 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.CharField(attrs={'class': 'form-control'}),
        #     'password2': forms.CharField(attrs={'class': 'form-control'}),
        #     'gender': forms.Select(attrs={'class': 'form-check form-check-inline'}),

        # }

class User_pw_form(forms.ModelForm):
    class Meta:
        model = User_pw
        fields = '__all__'
