from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone = models.CharField("Phone", max_length=255)


class PlayList(models.Model):
    url = models.CharField("PlayListURL", max_length=355)