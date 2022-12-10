"""scrapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.utils.translation import gettext_lazy as _
# from django.contrib.staticfiles.urls import static
# from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('company/', include('company.urls')),
    path('api/auth/', include('apiauthentication.urls')),
    path('api/company/', include('apicompany.urls')),
    path('api/experience/', include('apiexperience.urls')),
    path('reportcompany/', include('reportcompany.urls')),
    path('reportexperience/', include('reportexperience.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# admin.site.index_title = _('NCh Index')
# admin.site.site_header = _('Scraper Site Administration')
# admin.site.site_title = _('NCh Site Management')
