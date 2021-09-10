from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('api/v1/', include('puppies.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
