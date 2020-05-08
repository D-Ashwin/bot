from django.contrib import admin
from .models import UserProfile, PlayList

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PlayList)