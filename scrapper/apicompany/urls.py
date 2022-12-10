import imp
from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
router.register(r'get-company', Company_detail, basename='get_company')
router.register(r'get-all-companies', AllCompaniesViews, basename='all_companies')
router.register(r'get-all-companys-children', AllCompaniesViews, basename='all_companys-children')
# router.register(r'get-my-added-companies', MyCompaniesViews, basename='my_companies')

# specify URL Path for rest_framework
urlpatterns = [
    path('add-company', views.Company_add),
    path('delete-child-company/<int:pk>', views.childCompany_delete),
    path('delete-company-with-children/<int:pk>', views.Company_delete_with_children),
    path('update-company/<int:pk>', views.Company_update),
    path('', include(router.urls)),
]
