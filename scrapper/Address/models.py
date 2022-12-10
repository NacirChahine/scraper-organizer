from django.db import models
# from django.contrib import admin


class Country(models.Model):
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default='', blank=True)
    descriptionar = models.CharField(max_length=250, default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Region(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=False)
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
