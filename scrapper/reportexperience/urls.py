from django.urls import path
from .views import *


urlpatterns = [
    path('company-experiences-print', printAllCompanyChildren.as_view(), name='company_experiences_print'),
    path('company-experiences', getAllCompanyexpes, name='company_experience'),  # /<int:product_id>
]
