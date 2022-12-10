from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.
admin.site.register(Category,)
admin.site.register(ParentSector,)


# class SectorAdmin(admin.ModelAdmin):
#     fields = ('name', )

admin.site.register(Sector,)
admin.site.register(ChildCompanySector,)


@admin.register(Page)
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['company', 'url', ]  # li badi yehon ybayu
    list_display_links = ['company', ]  # li iza f2aset 3layon ye5duni 3laya
    list_editable = ['url', ]  # li fini 3adel 3layon
    search_fields = ['company__name', 'url', ]  # wen bi barrem


@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'overview', 'email', 'since']  # li badi yehon ybayu
    list_display_links = ['name', ]  # li iza f2aset 3layon ye5duni 3laya
    list_editable = ['overview', 'email']  # li fini 3adel 3layon
    search_fields = ['name', 'email', ]  # wen bi barrem


@admin.register(ChildCompany)
class ChildCompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['company', 'city', 'nbReviews', 'phoneNb', 'ranking']  # li badi yehon ybayu
    list_display_links = ['company', ]  # li iza f2aset 3layon ye5duni 3laya
    list_editable = ['city', 'nbReviews', 'phoneNb', 'ranking']  # li fini 3adel 3layon
    search_fields = ['company__name', 'city__name', 'phoneNb']  # wen bi barrem
    inlines = (ChildCompany_Sector_Inline,)
