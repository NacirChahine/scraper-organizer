from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'phone', 'about',)
    filter = ('name', 'email')
    list_display = ['name', 'email', 'phone', ]  # li badi yehon ybayu
    list_display_links = ['name', ]  # li iza f2aset 3layon ye5duni 3laya
    list_editable = ['email', 'phone', ]  # li fini 3adel 3layon
    search_fields = ['name', 'email', 'phone']  # wen bi barrem


class ExperienceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # fields = ('company', 'overview', 'email', 'since', 'website', 'country',)
    list_display = ['contact', 'role', 'company', ]  # li badi yehon ybayu
    list_display_links = ['contact', ]  # li iza f2aset 3layon ye5duni 3laya
    # list_editable = ['email', 'phone',]  # li fini 3adel 3layon
    search_fields = ['contact__name', 'role__name', 'company__name', ]  # wen bi barrem


admin.site.register(Contact, ContactAdmin)
admin.site.register(Role,)
admin.site.register(Experience, ExperienceAdmin)
