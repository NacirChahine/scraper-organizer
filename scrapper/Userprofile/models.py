from django.db import models
from django.contrib.auth.models import User
from Address.models import City
# from django.contrib import admin


# Create your models here.
class UserProfile1(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile1')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    # street = models.ForeignKey(Street, on_delete=models.PROTECT,null=True,blank=True)
    admin = models.BooleanField(default=False)
    profilePic = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
