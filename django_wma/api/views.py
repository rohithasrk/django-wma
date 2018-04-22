from rest_framework import viewsets
from .serializers import ContainerSerializer, WaterQualitySerializer, WaterQuantitySerializer
import swapper

Container = swapper.load_model('django_wma', 'Container')
WaterQuality = swapper.load_model('django_wma', 'WaterQuality')
WaterQuantity = swapper.load_model('django_wma', 'WaterQuantity')


class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer


class WaterQualityViewSet(viewsets.ModelViewSet):
    queryset = WaterQuality.objects.all()
    serializer_class = WaterQualitySerializer


class WaterQuantityViewSet(viewsets.ModelViewSet):
    queryset = WaterQuantity.objects.all()
    serializer_class = WaterQuantitySerializer
