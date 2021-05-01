from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = Choices('male', 'female', 'other')
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=32)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
