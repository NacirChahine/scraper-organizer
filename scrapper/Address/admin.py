from django.contrib import admin
from .models import *

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    fields = ('name', )

class ProvinceAdmin(admin.ModelAdmin):
    fields = ('country', 'name',)

class CityAdmin(admin.ModelAdmin):
    fields = ('province', 'name',)

class RegionAdmin(admin.ModelAdmin):
    fields = ('city', 'name',)

class StreetAdmin(admin.ModelAdmin):
    fields = ('region', 'name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Street, StreetAdmin)

