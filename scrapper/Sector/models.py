from django.db import models
from django.contrib.auth.models import User
# from django.contrib import admin
from django.contrib import admin
from Address.models import City


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class ParentSector(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Parent Sectors"  # parent

    def __str__(self):
        return self.name


class Sector(models.Model):
    # company = models.ForeignKey("Company", on_delete=models.PROTECT)
    parentSector = models.ForeignKey(ParentSector, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=True)
    chiledCompany = models.ManyToManyField('ChildCompany', through='ChildCompanySector')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sectors"

    def __str__(self):
        return self.name


#############Company###################
class Company(models.Model):
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=250, blank=True)
    overview = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    since = models.DateField()
    # website = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class ChildCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    nbReviews = models.IntegerField(blank=True)
    phoneNb = models.CharField(max_length=50, blank=True)
    ranking = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Child Companies"

    def __str__(self):
        return self.company.name


class ChildCompanySector(models.Model):  # mumken l company tkun bi kaza field aw kaza sector
    child_company = models.ForeignKey(ChildCompany, on_delete=models.PROTECT)
    Sector = models.ForeignKey(Sector, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Company Sectors"

    def __str__(self):
        return self.child_company.company.name + " of " + self.child_company.city.name + " - Sector: " + self.Sector.name


class ChildCompany_Sector_Inline(admin.TabularInline):
    model = ChildCompanySector
    extra = 1


class Page(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "company pages"

    def __str__(self):
        return self.company.name
