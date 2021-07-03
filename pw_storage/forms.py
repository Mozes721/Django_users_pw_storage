from django.forms import ModelForm
from django.forms import fields 
from .models import User, User_pw 
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegistrationForm(forms.Form):
    GENDER_CHOICES = [('male', 'male'), ('female','female'), ('other','other')]
    username = forms.CharField(max_length=15, label="Username")
    firstname = forms.CharField(max_length=15,label="Firstname")
    lastname = forms.CharField(max_length=15,label="Lastname")
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password Confirmation")
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES), max_length=6, required=True)

    class Meta:
        fields = '__all__'
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.CharField(attrs={'class': 'form-control'}),
        #     'password2': forms.CharField(attrs={'class': 'form-control'}),
        #     'gender': forms.Select(attrs={'class': 'form-check form-check-inline'}),

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

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    # def clean(self):
    #     data = super().clean()
    #     username = data.get("username")
    #     password = data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username

# class LoginForm(forms.ModelForm):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError("Username does not exists")
#             if user.checkpassword(password):
#                 raise forms.ValidationError("Wrong Password")
                
#     class Meta:
#         model = User
#         fields = ('username', 'password')

class User_pw_form(ModelForm):
    class Meta:
        model = User_pw
        fields = '__all__'

