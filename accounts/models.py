from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    image = models.ImageField(default='images.jpg',upload_to='profile picture',blank=True,null=True)
    Address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.username

