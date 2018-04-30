from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('django_wma.api.urls')),
    url(r'', include('django_wma.visualizer.urls')),
]
