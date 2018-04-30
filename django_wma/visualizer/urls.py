from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.container_list, name='container_list'),
    url(r'^container/(?P<pk>[^/]+)/$', views.container_detail, name='container_detail'),
]