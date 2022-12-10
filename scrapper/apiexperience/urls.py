# import imp
from django.urls import include, path
# importing routers
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
# define the router
router.register(r'get-experience-detail', experience_detail, basename='get_experience')
router.register(r'get-company-experiences', getAllexperienceOfCompanyViews, basename='get_company_experiences')
# router.register(r'get-my-added-companies', MyCompaniesViews, basename='my_companies')

# specify URL Path for rest_framework
urlpatterns = [
    path('add-experience', views.Experince_add),
    path('delete-experience/<int:pk>', views.experience_delete),
    path('update-experience/<int:pk>', views.experience_update),
    path('', include(router.urls)),
]
