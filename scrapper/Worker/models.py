from django.db import models
# from django.contrib.auth.models import User
# from django.contrib import admin
from Sector.models import Company


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    about = models.TextField(max_length=250, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    fromDate = models.DateField()
    toDate = models.DateField()
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Experiences"

    def __str__(self):
        return self.contact.name + ': ' + self.role.name
