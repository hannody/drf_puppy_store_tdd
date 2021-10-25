from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django_otp.admin import OTPAdminSite
from decouple import config

from core import settings

if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite
    ADMIN_URL = config('ADMIN_URL')
else:
    ADMIN_URL = 'admin'


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/v1/', include('puppies.urls')),
    path(ADMIN_URL, admin.site.urls),
]