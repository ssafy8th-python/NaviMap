from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=100, null=True)
    profile_image = models.TextField(blank=True)
    thumbnail_image = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    refresh_token = models.TextField(blank=True)