from django.urls import path
from .views import *


urlpatterns = [
    path('child-companies-print', printAllCompanyChildren.as_view(), name='chiled_companies_print'),
    path('child-companies', getAllCompanyChilds, name='chiled_companies'),  # /<int:product_id>
]
