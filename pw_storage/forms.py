from django.forms import ModelForm
from django.forms import fields 
from .models import User, User_pw 
from django import forms

class UserForm(ModelForm):
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
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user_email = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'Email "%s" is already in use.' % email)

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


    # widgets = {
    #     'username': ModelForm.TextInput(attrs={'class': 'form-control'}),
    #     'password': ModelForm.PasswordInput(attrs={'class': 'form-control'}),
    # }
  
    # def check_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         user = User.objects.exclude(pk=self.instance.pk).get(username=username)
    #     except User.DoesNotExist:
    #         return username
    #     raise forms.ValidationError(u'Username "%s" does not exist.' % username)

    # def check_password(self):
    #     password = self.cleaned_data['password']
    #     try:
    #         user_pw = User.objects.exclude(pk=self.instance.pk).get(password=password)
    #     except User.DoesNotExist:
    #         return password
    #     raise forms.ValidationError('Password is invalid')  

class User_pw_form(ModelForm):
    class Meta:
        model = User_pw
        fields = '__all__'
