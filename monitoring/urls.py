from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django_wma import urls as water_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(water_urls)),
]
