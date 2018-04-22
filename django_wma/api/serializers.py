import swapper
from rest_framework import serializers


class AllFieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'


class ContainerSerializer(AllFieldSerializer):
    class Meta(AllFieldSerializer.Meta):
        model = swapper.load_model('django_wma', 'Container')


class WaterQualitySerializer(AllFieldSerializer):
    class Meta(AllFieldSerializer.Meta):
        model = swapper.load_model('django_wma', 'WaterQuality')


class WaterQuantitySerializer(AllFieldSerializer):
    class Meta(AllFieldSerializer.Meta):
        model = swapper.load_model('django_wma', 'WaterQuantity')
