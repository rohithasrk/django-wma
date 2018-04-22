from django.conf.urls import url, include
from .views import index

urlpatterns = [
    url(r'^api/', include('django_wma.api.urls')),
    url(r'', index, name='index'),
]
