from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

admin_url = 'd788b92cc1c9681bedee6a6fa9f67c33ae2f382251db8a620f83b09c50faad32/'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/v1/', include('puppies.urls')),
    path(admin_url, admin.site.urls),
]