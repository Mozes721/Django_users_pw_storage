from django.forms import ModelForm
from django.forms import fields 
from .models import User, User_pw 
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    GENDER_CHOICES = [('male', 'male'), ('female','female'), ('other','other')]
    username = forms.CharField(max_length=15, label="Username")
    firstname = forms.CharField(max_length=15,label="Firstname")
    lastname = forms.CharField(max_length=15,label="Lastname")
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password Confirmation")
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES), max_length=6, required=True)

    class Meta:
        model = User
        fields = ("username", "firstname", "lastname", "email", 
     "password", "password1","gender")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise ValidationError("Username already exists")
        return username

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise ValidationError("Password didn't match")
        return password1

class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username does not exists")
            if user.checkpassword(password):
                raise forms.ValidationError("Wrong Password")
                
    class Meta:
        model = User
        fields = ("username", "password")

class User_pw_form(ModelForm):
    class Meta:
        model = User_pw
        fields = '__all__'

