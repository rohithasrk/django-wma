from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'containers', views.ContainerViewSet)
router.register(r'waterquality', views.WaterQualityViewSet)
router.register(r'waterquantity', views.WaterQuantityViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]