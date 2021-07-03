from django.db import models
from django.db.models.deletion import CASCADE
from django import forms
from django.core.exceptions import ValidationError


# Create your models here.
# class User(models.Model):
#     GENDER_CHOICES = [('male', 'male'), ('female','female'), ('other','other')]
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100, blank=False)
#     firstname = models.CharField(max_length=80, blank=False)
#     lastname = models.CharField(max_length=80, blank=False)
#     email = models.EmailField(max_length=150, blank=False)
#     password = models.CharField(max_length=30)
#     password1 = models.CharField(max_length=30)
#     gender = models.CharField(choices=GENDER_CHOICES, max_length=6, blank=False)

#     def __str__(self):
#         return self.username

#     class User_login(models.Model):
#         pass
    
# class User_pw(models.Model):
#     headline = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)
#     user = models.ForeignKey(User, on_delete=CASCADE)

#     def __str__(self):
#         return self.headline

#     class Meta:
#         ordering = ['headline']
