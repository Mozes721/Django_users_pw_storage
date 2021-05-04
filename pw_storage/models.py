from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = [('male', 'male'), ('female','female'), ('other','other')]
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=32)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)

    def __str__(self):
        return self.username

    
class User_pw(models.Model):
    headline = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
