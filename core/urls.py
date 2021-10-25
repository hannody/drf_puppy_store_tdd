from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django_otp.admin import OTPAdminSite
from decouple import config

if config('DEBUG'):
    ADMIN_URL = 'admin'
else:
    # Enforce 2FA only in production.
    admin.site.__class__ = OTPAdminSite
    # Use a more secure admin url instead of the default 'admin'
    ADMIN_URL = config('ADMIN_URL')

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/v1/', include('puppies.urls')),
    path(ADMIN_URL, admin.site.urls),
]