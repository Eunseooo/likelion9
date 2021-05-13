from django.db import models

# Create your models here.

class You(models.Model):
    your_Major= models.CharField(max_length=200)
    your_Favorite = models.CharField(max_length=100)
    your_Gender = models.CharField(max_length=200)
    your_Birthday = models.DateTimeField()
    introduce_me_to_you = models.TextField()