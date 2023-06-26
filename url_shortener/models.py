from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=20,unique=True)
    userName=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

#the below is our table which will store all the URL's data
class LongtoShort(models.Model):
    user_id=models.CharField(max_length=20)
    long_url = models.URLField(max_length=500)
    custom_name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    clicks = models.IntegerField(default=0)


# class UserModel(models.Model):
   

